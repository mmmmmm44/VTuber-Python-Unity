"""
Miscellaneous facial features detection implementation
"""

import cv2
import numpy as np
from enum import Enum

class Eyes(Enum):
    LEFT = 1
    RIGHT = 2

class FacialFeatures:

    eye_key_indicies=[
        [
        # Left eye
        # eye lower contour
        33,
        7,
        163,
        144,
        145,
        153,
        154,
        155,
        133,
        # eye upper contour (excluding corners)
        246,
        161,
        160,
        159,
        158,
        157,
        173
        ],
        [
        # Right eye
        # eye lower contour
        263,
        249,
        390,
        373,
        374,
        380,
        381,
        382,
        362,
        # eye upper contour (excluding corners)
        466,
        388,
        387,
        386,
        385,
        384,
        398
        ]
    ]

    # custom img resize function
    def resize_img(img, scale_percent):
        width = int(img.shape[1] * scale_percent / 100.0)
        height = int(img.shape[0] * scale_percent / 100.0)

        return cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)

    def detect_iris(img, marks, side):
        """
        return:
           x: the x coordinate of the iris in the input image.
           y: the y coordinate of the iris in the input image.
           x_rate: how much the iris is toward the left. 0 means totally left and 1 is totally right.
           y_rate: how much the iris is toward the top. 0 means totally top and 1 is totally bottom.
        """

        # change the value here to suit your camera/ eye
        left_eye_threshold = 34
        right_eye_threshold = 45

        mask = np.full(img.shape[:2], 255, np.uint8)

        region = None

        if side == Eyes.LEFT:
            region = np.zeros((len(FacialFeatures.eye_key_indicies[0]), 2), np.int32)

            # get the pixel of the eyes region
            for i in range(region.shape[0]):
                region[i, 0] = marks[FacialFeatures.eye_key_indicies[0][i]][0]
                region[i, 1] = marks[FacialFeatures.eye_key_indicies[0][i]][1]

        elif side == Eyes.RIGHT:
            region = np.zeros((len(FacialFeatures.eye_key_indicies[1]), 2), np.int32)

            for i in range(region.shape[0]):
                region[i, 0] = marks[FacialFeatures.eye_key_indicies[1][i]][0]
                region[i, 1] = marks[FacialFeatures.eye_key_indicies[1][i]][1]

        try:
            cv2.fillPoly(mask, [region], (0, 0, 0))
            eye = cv2.bitwise_not(img, img.copy(), mask=mask)

            # Cropping on the eye
            margin = 4
            min_x = np.min(region[:, 0]) - margin
            max_x = np.max(region[:, 0]) + margin
            min_y = np.min(region[:, 1]) - margin
            max_y = np.max(region[:, 1]) + margin

            eye = eye[min_y:max_y, min_x:max_x]

            # filtering
            eye_gray = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)

            eye_gray = cv2.GaussianBlur(eye_gray, (5, 5), 0)
            cv2.imshow("left eye gray" if side == Eyes.LEFT else "right eye gray",
                FacialFeatures.resize_img(eye_gray, 300))

            # TODO:
            # follow tutorial for eye-motion tracking
            # https://youtu.be/kbdbZFT9NQI

            # threshold the image to show the pupil roi
            _, threshold = cv2.threshold(eye_gray,
                left_eye_threshold if side == Eyes.LEFT else right_eye_threshold,
                255, cv2.THRESH_BINARY_INV)

            cv2.imshow("left eye threshold" if side == Eyes.LEFT else "right eye threshold", threshold)

            # search for contours and get the largest one
            contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse = True)
            cnt = contours[0]
            cv2.drawContours(eye, [cnt], 0, (0, 255, 0), 1)

            # get the contour box, and get its x and y position
            (x, y, w, h) = cv2.boundingRect(cnt)
            x_center, y_center = x + int(w / 2), y + int(h / 2)

            # drawing
            cv2.rectangle(eye, (x, y), (x+w, y+h), (255, 0, 0), 1)
            cv2.line(eye, (x_center, 0), (x_center, eye.shape[0]), (0, 255, 0), 1)
            cv2.line(eye, (0, y_center), (eye.shape[1], y_center), (0, 255, 0), 1)

            # print("%d, %d, %d, %d" % (min_x + margin, max_x - margin, min_y + margin, max_y - margin))
            # print("right eye: %d, %d, %.2f, %.2f" % (x_right, y_right, x_ratio_right, y_ratio_right))

            # calculate the ratio
            x_ratio = np.clip(x_center / (max_x - min_x - margin * 2), 0, 1)
            y_ratio = np.clip(y_center / (max_y - min_y - margin * 2), 0, 1)

            cv2.imshow("left eye" if side == Eyes.LEFT else "right eye",
                FacialFeatures.resize_img(eye, 300))

            return x_center + (min_x - margin), y_center + (min_y - margin), x_ratio, y_ratio

        except:
            return 0, 0, 0.5, 0.5
