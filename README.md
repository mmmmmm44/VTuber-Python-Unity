# VTuber Python Unity Tutorial

An Implementation of VTuber (Both 3D and Live2D) using Python and Unity. Supporting **face movement tracking**, **eye blinking detection**, **iris detection and tracking** and **mouth movement tracking** using **CPU only**.

## Usage
![Live2D Demo](https://github.com/mmmmmm44/VTuber-Python-Unity/blob/main/Images/live2d_demo.gif)

*Live2D Demo*

![UnityChan 3D Demo](https://github.com/mmmmmm44/VTuber-Python-Unity/blob/main/Images/unitychan3d_demo.gif)

*UnityChan 3D Demo*

## Features
* Facial landmarks detection and movement tracking supported by Facemesh by [Mediapipe](https://github.com/google/mediapipe).
* Various facial expressions detection including eye blinking, iris and mouth movements.
* Running **smooth 30 FPS** with **CPU only** for the aformentioned features.
* Simple and clean UI for adjusting the sensibility of detection in Unity.
* Saveload mechanism to save and load your preferences in Unity.
* Including sample (Unity) projects for both 3D and Live2D models

*Due to Github file size limitation, most of the folders in the unity chan sample project are removed, yet the project can still run*

## File Explanation
|File|Description|
|:---:|:---:|
|main.py|The main program|
|facial_landmark.py|The module which is used to detect your face and generate the facial landmarks.|
|pose_estimator.py|The module which estimates your pose/ orientation of your head based on the landmarks.|
|stabilizer.py|Implementation of Kalman Filter to stabilize the values.|
|facial_features.py|Various facial features detection implementation, including blinking, iris detection and mouth movement.|
|model.txt|The points of the 3D Canonical model used in Mediapipe. [Source file](https://github.com/google/mediapipe/blob/master/mediapipe/modules/face_geometry/data/canonical_face_model.obj)|
|UnityAssets|Whole Unity Projects (in packages) and Scripts for both 3D (UnityChan) and Live2D (Hiyori) models|

## Background
Using avatars for streaming, content creation and VR gaming has been gaining increasing popularity, especially the boom of Hololive and other related companies active apperances in social media platforms such as YouTube and Twitter. Curious about the technology behind, I create this project after multiple researches.

Existing projects rely on Dlib, which although providing reliable and accurate facial landmark detection, requires decent graphic cards to run. However, implemented with the recent FaceMesh model in [Mediapipe](https://github.com/google/mediapipe), accurate detection and tracking can be run smoothly using CPU only, making running on computers with mediocre graphic cards or laptops with integrated graphic cards possible.

## How To Use
_As the "*.unitypackage" files are uploaded through github's LFS (Large File Storage) system, you may have to install the corresponding package to clone the project successfully. Click the [link](https://git-lfs.github.com/) for more information._

Clone this project into your directory

```
git clone
cd "VTuber-Python-Unity"
```

### Simple Setup
1. Create An empty Unity 3D Project

2. Import either the Live2D or UnityChan3D package to your project. The corresponding SDKs have been included already.

3. Run the Scene.

4. Run the following code in terminal
[content in the bracket is optional]
```
python main.py --connect [--debug]
```

5. Enjoy


### Custom Setup (For people who want to import their own 3D/ Live2D model)

#### For Live2D model
1. Download the Cubism SDK For Unity from this [website](https://www.live2d.com/download/cubism-sdk/) and the sample model used (桃瀬ひより) from this [website](https://www.live2d.com/download/sample-data/)

2. Create an empty Unity 3D project, and import the Cubism SDK. Unzip the model and drag the whole folder to the Project window of the Unity Project.

3. Drag the live2D model's prefab into the scene. Run the scene immediately to allow the model to be showed in Scene and Game window.

4. Adjust the camera's position, background and projection properties. If there are some werid projection problems of the model, changing the projection of the camera from Perspective and Orthographic works for me.

5. Drag the HiyoriController.cs to the Hiyori GameObject. Adjust the parameters in the inspector

6. Run the scene.

7. Run the following code in terminal
[content in the bracket is optional]
```
python main.py --connect [--debug]
```

8. Enjoy

#### For 3D Model (UnityChan)
1. Download the UnityChan model from the [website](https://unity-chan.com/). Go to "Data Download", accept the terms and agreements, and select the first one. Unzip the file.

2. Create an empty Unity 3D Project. Drag the unzipped folder to the Project Window of the project.

3. Go to UnityChan\Prefabs and Drag the "unitychan" prefab into the scene.

4. Adjust the camera's position, background and field of view.

5. Drag the UnityChanControl.cs script onto the prefab. Adjust the variables in the inspector. Disable other attached scripts except AutoBlink and UnityChanControl. You may disable the AutoBlink script attached to control the blinking by yourself.

6. Run the scene first

7. Run the following code in terminal
[content in the bracket is optional]
```
python main.py --connect [--debug]
```

8. Enjoy

**Make sure you run the Unity Scene first before running the python script**

*Both the python scripts and the unity project can be exported to .exe, which can be run on other computers.*

## Development Environment
* Python 3.8.5
* Numpy 1.19.2
* OpenCV 4.5.1
* Mediapipe 0.8.5

* Unity 2020.3.12f1

(Later version should be supported as well)

*(For Windows, it is recommended to run this project using Anaconda and create a virtual environment before installing such packages.)*

*The whole project is run on a laptop with Intel Core i5-8250U, with 16GB RAM and integrated graphic card only.*


## References/ Credits

[Detect 468 Face Landmarks in Real-time | OpenCV Python | Computer Vision - Murtaza's Workshop - Robotics and AI](https://youtu.be/V9bzew8A1tc)

[Eye motion tracking - Opencv with Python - Pysoruce](https://youtu.be/kbdbZFT9NQI)

 | Project | Author | LICENSE |
 |:---:|:---:|:---:|
 | [head-pose-estimation](https://github.com/yinguobing/head-pose-estimation) | [Yin Guobing](https://github.com/yinguobing) | [LICENSE](https://github.com/yinguobing/head-pose-estimation/blob/master/LICENSE) |
 | [VTuber_Unity](https://github.com/kwea123/VTuber_Unity) | [AI葵](https://github.com/kwea123) | [LICENSE](https://github.com/kwea123/VTuber_Unity/blob/master/LICENSE) |
 |[VTuber-MomoseHiyori](https://github.com/KennardWang/VTuber-MomoseHiyori) |[KennardWang](https://github.com/KennardWang)|[LICENSE](https://github.com/KennardWang/VTuber-MomoseHiyori/blob/master/LICENSE)|

Hiyori Momose's model
|Position|Creator|
|:---:|:---:|
|Illustration|Kani Biimu [Twitter [@kani_biimu](https://twitter.com/kani_biimu)]|
|Modeling|Live2D Inc.|

## License
MIT

The Unity Chan model in the Unity Packages provided is distributed under Unity-Chan License © Unity Technologies Japan/UCL. A seperate sets of that License is included in UnityAssets/Licenses/UCL2_0
