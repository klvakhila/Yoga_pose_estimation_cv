# Yoga Pose Estimation CV

This application leverages **OpenCV**, **Mediapipe**, and **Streamlit** to detect and classify yoga poses in real-time. It provides an interactive interface for both image-based and real-time webcam yoga pose analysis.

### Modes of Operation

1. **Image Mode**: Upload an image to detect and classify yoga poses from the uploaded image.
2. **Webcam Mode**: Use your device's webcam to detect and classify yoga poses in real-time.

### Features

- **Pose Detection**: Uses **Mediapipe's** pose estimation to identify key body landmarks in images or webcam feeds.
- **Pose Classification**: Classifies common yoga poses (e.g., Warrior II Pose, Tree Pose, T Pose) based on calculated joint angles.
- **Real-Time Feedback**: Offers immediate classification for live webcam streams.
- **Live Webcam Feed**: Displays the live webcam feed with detected poses annotated on the screen.
- **Image Upload**: Users can upload an image to detect and classify yoga poses, with corresponding feedback provided.

### Technologies Used

- **Python**: Core language used for app development.
- **Streamlit**: Framework for building the interactive frontend for the app.
- **OpenCV**: Image and video processing library used for working with images and capturing live feed from the webcam.
- **Mediapipe**: Google’s library that helps in detecting and locating human body landmarks for pose estimation.
- **NumPy**: Python library to handle and process data arrays efficiently for image manipulation.

### Instructions to Run

1. **Clone or download** the repository.

2. **Install required dependencies**:
   ```bash
   pip install streamlit opencv-python mediapipe numpy
3. **Run**:
   ```bash
   streamlit run app.py


