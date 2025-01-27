# Yoga_pose_estimation_cv
Yoga pose  estimation  using computer vision
Yoga Pose Detection App
This app leverages OpenCV, Mediapipe, and Streamlit to detect and classify yoga poses in real-time. It provides two modes of operation:

Image Mode: Upload an image to detect yoga poses.
Webcam Mode: Use the webcam to detect and classify yoga poses live.
Features
Pose Detection: Uses Mediapipe's pose estimation to identify key body landmarks.
Pose Classification: Classifies common yoga poses (e.g., Warrior II Pose, Tree Pose, T Pose) based on calculated joint angles.
Real-Time Feedback: Offers real-time classification for video streams using the webcam.
Live Webcam Feed: Displays the live webcam feed with pose annotations directly within the Streamlit interface.
Image Upload: Allows users to upload an image for pose detection, along with visual feedback.
Technologies Used
Python: Primary programming language used for app development.
Streamlit: A Python library used to build the user interface for the app.
OpenCV: Used for image and video processing.
Mediapipe: A Google library that provides robust pose estimation for detecting and locating body landmarks.
NumPy: Used for efficient handling of image data as arrays.
Instructions to Run
Clone or download the repository.

Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt file, install necessary libraries manually:

bash
Copy
Edit
pip install streamlit opencv-python mediapipe numpy
Run the app:

bash
Copy
Edit
streamlit run app.py
Usage:

For Image Mode, upload an image through the provided file uploader to detect yoga poses.
For Webcam Mode, press the checkbox to start the webcam, and the app will classify your yoga poses live.
The pose name will be displayed on the screen alongside the live feed or processed image.

Pose Classifications
Warrior II Pose: Identified by specific joint angle ranges.
T Pose: Characterized by specific angles between the elbows and shoulders.
Tree Pose: Distinguished by angles in the knees and hips.
The app can detect if a yoga pose is done incorrectly by marking it as "Wrong Pose" when the angles don't match the specified ranges.

