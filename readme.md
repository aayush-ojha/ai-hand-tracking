
# Hand Detection Application

This application uses the MediaPipe library to detect hands in images, videos, and live camera feeds. It can also take a photo when a specific hand pose (the "cheese pose" with two fingers extended) is detected in the live camera feed.

## Requirements

- Python 3.6+
- OpenCV
- MediaPipe

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aayush-ojha/hand-detection-app.git
    cd hand-detection-app
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python mediapipe
    ```

## Usage

Run the application:
```bash
python main.py
```

You will be prompted to choose a mode:
- Enter `image` to load from an image file.
- Enter `video` to load from a video file.
- Enter `live` to use the live camera feed.

### Image Mode

When prompted, enter the path to the image file. The application will display the image with detected hands.

### Video Mode

When prompted, enter the path to the video file. The application will play the video with detected hands.

### Live Camera Mode

The application will use the live camera feed to detect hands. If the "cheese pose" (two fingers extended) is detected, a photo will be taken and saved with a timestamp.

## Example

```bash
Enter 'image' to load from image, 'video' to load from video, or 'live' to use live camera: live
```

In live camera mode, if the "cheese pose" is detected, you will see output like:
```bash
Photo taken: cheese_pose_1634567890.png
```

## License

This project is licensed under the MIT License.
