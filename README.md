# Hand Gesture Door Lock

A Python project that uses hand gestures to unlock a door.

## Description

This project utilizes computer vision and hand-tracking techniques to detect hand gestures and unlock a door based on a predefined password. The project uses the OpenCV library for video capture and image processing, and it includes a custom module called HandTrackingModule for hand tracking and gesture recognition.


## HandGesture By One Hande

You can see the hand gesture for every number in one hand from the HandGestures folder


## Features

- Detects hand gestures in real-time using a webcam.
- Recognizes hand gestures corresponding to numbers 0 to 10.
- Compares the detected hand gesture sequence with a predefined password.
- Unlocks the door if the password is correctly matched.

## Requirements

- Python 3.x
- OpenCV
- mediapipe

## How to Use

1. Ensure you have Python 3.x installed on your system.
2. Install the required Python libraries by running the following command:
3. Clone this repository to your local machine or download the project files.
4. Open the terminal or command prompt and navigate to the project directory.
5. Run the "HandGestureDoorLock.py" script:
6. A new window displaying the webcam feed with hand tracking and gesture recognition will open.
7. Follow the on-screen instructions to unlock the door using hand gestures.

## Configuration

- You can adjust the webcam resolution by modifying the `wCam` and `hCam` variables in the "HandGestureDoorLock.py" script.
- The predefined password is set using the `password` list in the script. You can modify it according to your desired password.

## Acknowledgments

This project is built using the following libraries and modules:

- OpenCV: https://opencv.org/
- mediapipe: https://mediapipe.dev/

The "HandTrackingModule.py" module is a custom module developed for this project and provides hand-tracking and gesture-recognition functionalities.
