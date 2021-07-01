# VTuber Python Unity Tutorial

An Implementation of VTuber (Both 3D and Live2D) using Python and Unity. Supporting **face movement tracking**, **eye blinking detection**, **iris detection and tracking **and **mouth movement tracking**.

## Usage
(Include a Demo)

## File Explanation
|File|Description|
 |:---:|:---:|:---:|
 |main.py|The main program|
 |facial_landmark.py|The module which is used to detect your face and generate the facial landmarks.|
 |pose_estimator.py|The module which estimates your pose/ orientation of your head based on the landmarks.|
 |stabilizer.py|Implementation of Kalman Filter to stabilize the values.|
 |facial_features.py|Various facial features detection implementation, including blinking, iris detection and mouth movement.|
 |UnityAssets|Scripts for both 3D (UnityChan) and Live2D (Hiyori) models|

## Background
Using avatars for streaming, content creation and VR gaming has been gaining increasing popularity, especially the boom of Hololive and other related companies active apperances in social media platforms such as YouTube and Twitter. Curious about the technology behind, I create this project after multiple researches.

Existing projects rely on Dlib, which although providing reliable and accurate facial landmark detection, requires decent graphic cards to run. However, implementing with the recent FaceMesh model in [Mediapipe](https://github.com/google/mediapipe), the detection can run smoothly using CPU only, making running on computers with mediocre graphic cards or laptops with integrated graphic cards possible.

## How To Use
Clone this project into your directory
```
git clone
cd
```
### For Live2D model
1. Download the Cubism SDK For Unity from this [website](https://www.live2d.com/download/cubism-sdk/) and the sample model used (桃瀬ひより) from this [website](https://www.live2d.com/download/sample-data/)

2. Create an empty Unity 3D project, and import the Cubism SDK. Unzip the model and drag the whole folder to the Project window of the Unity Project.

3. Drag the live2D model's prefab into the scene, and adjust the camera's position, background and projection properties. If there are some werid projection errors of the model, changing the projection of the camera from Perspective and Orthographic works for me.

4. Drag the HiyoriController.cs to the Hiyori GameObject. Adjust the Parameters in the inspector

5.  Run the Scene

6. Run the following code in terminal
[content in the bracket is optional]
```
python main.py --connect [--debug]
```

7. Enjoy

### For 3D Model (UnityChan)
1. Download the UnityChan model from the [website](https://unity-chan.com/). Go to "Data Download", accept the terms and agreements, and select the first one. Unzip the file.

2. Create an empty Unity 3D Project. Drag the unzipped folder to the Project Window of the project.

3. Go to UnityChan\Prefabs and Drag the "unitychan" prefab into the scene.

4. Adjust the camera's position, background and field of view.

5. Drag the UnityChanControl.cs script onto the prefab. Adjust the variables in the inspector. You may disable the AutoBlink script attached to control the blinking by yourself.

6. Run the scene first

7. Run the following code in terminal
[content in the bracket is optional]
```
python main.py --connect [--debug]
```

8. Enjoy

**Make sure you run the Unity Scene first before running the python script**

## Development Environment
* Python 3.8.5
* Numpy 1.19.2
* OpenCV 4.5.1
* Mediapipe 0.8.5

* Unity 2020.3.12f1

(Later version should be supported as well)

(For Windows, it is recommended to run this project using Anaconda and create a virtual environment before installing such packages.)


## References
 | Project | Author | LICENSE |
 |:---:|:---:|:---:|
 | [head-pose-estimation](https://github.com/yinguobing/head-pose-estimation) | [Yin Guobing](https://github.com/yinguobing) | [LICENSE](https://github.com/yinguobing/head-pose-estimation/blob/master/LICENSE) |
 | [VTuber_Unity](https://github.com/kwea123/VTuber_Unity) | [AI葵](https://github.com/kwea123) | [LICENSE](https://github.com/kwea123/VTuber_Unity/blob/master/LICENSE) |
 |[VTuber-MomoseHiyori](https://github.com/KennardWang/VTuber-MomoseHiyori) |[KennardWang](https://github.com/KennardWang)|[LICENSE](https://github.com/KennardWang/VTuber-MomoseHiyori/blob/master/LICENSE)|

 [Eye motion tracking - Opencv with Python - Pysoruce](https://youtu.be/kbdbZFT9NQI)

[Detect 468 Face Landmarks in Real-time | OpenCV Python | Computer Vision - Murtaza's Workshop - Robotics and AI](https://youtu.be/V9bzew8A1tc)

## License
MIT
