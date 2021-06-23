"""
Main program to run the detection
"""

import cv2
import mediapipe as mp
import numpy as np

# for TCP connection with unity
import socket
from collections import deque
from platform import system

from pose_estimator import PoseEstimator
from stabilizer import Stabilizer

connect = True
port = 5066         # have to be same as unity

# init TCP connection with unity
# return the socket connected
def init_TCP():
    address = ('127.0.0.1', port)
    # address = ('192.168.0.107', port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print(socket.gethostbyname(socket.gethostname()))
    s.connect(address)
    return s

def send_info_to_unity(s, args):
    msg = '%.4f %.4f %.4f' % args
    s.send(bytes(msg, "utf-8"))


def main():

    cap = cv2.VideoCapture(0)

    # Facemesh
    mp_face_mesh = mp.solutions.face_mesh
    # The object to do the stuffs
    face_mesh = mp_face_mesh.FaceMesh()

    mp_drawing = mp.solutions.drawing_utils
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

    # get a sample frame for pose estimation img
    success, img = cap.read()

    # Pose estimation related
    pose_estimator = PoseEstimator((img.shape[0], img.shape[1]))
    image_points = np.zeros((pose_estimator.model_points_full.shape[0], 2))

    # Introduce scalar stabilizers for pose.
    pose_stabilizers = [Stabilizer(
        state_num=2,
        measure_num=1,
        cov_process=0.1,
        cov_measure=0.1) for _ in range(6)]


    # Initialize TCP connection
    if connect:
        socket = init_TCP()

    while cap.isOpened():
        success, img = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            continue

        # convert the img from BRG to RGB
        img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        img.flags.writeable = False
        results = face_mesh.process(img)

        # Draw the face mesh annotations on the image.
        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        imgH, imgW, imgC = img.shape

        # Pose estimation by 3 steps:
        # 1. detect face;
        # 2. detect landmarks;
        # 3. estimate pose

        # Here is the first two steps
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image = img,
                    landmark_list = face_landmarks,
                    connections = mp_face_mesh.FACE_CONNECTIONS,
                    landmark_drawing_spec = drawing_spec,
                    connection_drawing_spec = drawing_spec)

                # print(face_landmarks)

                for id, lmk in enumerate(face_landmarks.landmark):
                    x, y = int(lmk.x * imgW), int(lmk.y * imgH)
                    image_points[id, 0] = x
                    image_points[id, 1] = y

            # The third step: pose estimation
            # pose: [[rvec], [tvec]]
            pose = pose_estimator.solve_pose_by_all_points(image_points)

            # print("rvec (y) = (%f): " % (pose[0][1]))
            # print("rvec (x, y, z) = (%f, %f, %f): " % (pose[0][0], pose[0][1], pose[0][2]))
            # print("tvec (x, y, z) = (%f, %f, %f): " % (pose[1][0], pose[1][1], pose[1][2]))

            # Stabilize the pose.
            steady_pose = []
            pose_np = np.array(pose).flatten()

            for value, ps_stb in zip(pose_np, pose_stabilizers):
                ps_stb.update([value])
                steady_pose.append(ps_stb.state[0])

            steady_pose = np.reshape(steady_pose, (-1, 3))

            # print("rvec (x, y, z) = (%f, %f, %f): " % (steady_pose[0][0], steady_pose[0][1], steady_pose[0][2]))
            # print("tvec steady (x, y, z) = (%f, %f, %f): " % (steady_pose[1][0], steady_pose[1][1], steady_pose[1][2]))


            # calculate the roll/ pitch/ yaw
            # roll: +ve when the axis pointing upward
            # pitch: +ve when we look upward
            # yaw: +ve when we look left
            roll = np.clip(np.degrees(steady_pose[0][1]), -90, 90)
            pitch = np.clip(-(180 + np.degrees(steady_pose[0][0])), -90, 90)
            yaw =  np.clip(np.degrees(steady_pose[0][2]), -90, 90)

            print("Roll: %.2f, Pitch: %.2f, Yaw: %.2f" % (roll, pitch, yaw))

            # send info to unity
            if connect:
                send_info_to_unity(socket, (roll, pitch, yaw))


            # pose_estimator.draw_annotation_box(img, pose[0], pose[1], color=(255, 128, 128))

            # pose_estimator.draw_axis(img, pose[0], pose[1])

            pose_estimator.draw_axes(img, steady_pose[0], steady_pose[1])

        else:
            # reset our pose estimator
            pose_estimator = PoseEstimator((img.shape[0], img.shape[1]))




        # flip vertically at the end for creating mirror img
        # img = cv2.flip(img, 1)
        cv2.imshow('MediaPipe FaceMesh', img)

        # press "q" to leave
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()


if __name__ == "__main__":
    # demo code
    main()
