import streamlit as st
import math
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

# Initialize Mediapipe Pose and Drawing Utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.1, model_complexity=2)
mp_drawing = mp.solutions.drawing_utils

# Function to Detect Pose and Return Results
def detect_pose(image, pose, display=True):
    output_image = image.copy()
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    height, width, _ = image.shape

    landmarks = []
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image=output_image, landmark_list=results.pose_landmarks, connections=mp_pose.POSE_CONNECTIONS
        )
        for landmark in results.pose_landmarks.landmark:
            landmarks.append(
                (int(landmark.x * width), int(landmark.y * height), (landmark.z * width))
            )
    return output_image, landmarks

# Function to Calculate Angle Between Joints
def calculateAngle(landmark1, landmark2, landmark3):
    x1, y1, _ = landmark1
    x2, y2, _ = landmark2
    x3, y3, _ = landmark3
    angle = math.degrees(
        math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2)
    )
    if angle < 0:
        angle += 360
    return angle

# Function to Classify Pose
def classifyPose(landmarks, output_image, display=False):
    label = 'Wrong Pose'
    color = (0, 0, 255)  # Default color: Red for unknown pose
    
    # Calculate angles for relevant joints
    left_elbow_angle = calculateAngle(
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value],
    )
    right_elbow_angle = calculateAngle(
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value],
    )
    left_shoulder_angle = calculateAngle(
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
    )
    right_shoulder_angle = calculateAngle(
        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
    )
    left_knee_angle = calculateAngle(
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value],
    )
    right_knee_angle = calculateAngle(
        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value],
    )

    # Classify poses based on angles
    if 165 < left_elbow_angle < 195 and 165 < right_elbow_angle < 195:
        if 80 < left_shoulder_angle < 120 and 80 < right_shoulder_angle < 120:
            if (165 < left_knee_angle < 195 or 165 < right_knee_angle < 195):
                if 90 < left_knee_angle < 120 or 90 < right_knee_angle < 120:
                    label = "Warrior II Pose"
                elif 160 < left_knee_angle < 195 or 160 < right_knee_angle < 195:
                    label = "T Pose"
    if 165 < left_knee_angle < 195 or 165 < right_knee_angle < 195:
        if 315 < left_knee_angle < 335 or 25 < right_knee_angle < 45:
            label = "Tree Pose"

    # Update label color to green for a recognized pose
    if label != "Wrong Pose":
        color = (0, 255, 0)
     # Add text to the image
    cv2.putText(output_image, label, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    # Display the output image
   
    return output_image, label

# Streamlit App
def main():
    st.title("Yoga Pose Detection App")
    st.write("This app detects yoga poses in real-time using OpenCV and Mediapipe.")

    # Sidebar
    st.sidebar.title("Options")
    mode = st.sidebar.selectbox("Choose Input Mode", ["Image", "Webcam"])

    # Image Input Mode
    if mode == "Image":
        uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            # Read and process the image
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1)
            output_image, landmarks = detect_pose(image, pose)
            if landmarks:
                output_image, label = classifyPose(landmarks, output_image)

            # Display the input and output images
            st.image(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB), caption="Processed Image", use_column_width=True)

    # Webcam Mode
    elif mode == "Webcam":
        camera_input = st.camera_input("Capture Video")
        if camera_input:
            frame = camera_input.image_data
            frame = np.array(frame)
            output_image, landmarks = detect_pose(frame, pose)
            if landmarks:
                output_image, label = classifyPose(landmarks, output_image)

            # Display the live video with detected pose
            st.image(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB), caption="Processed Webcam Frame", use_column_width=True)

# Run the Streamlit App
if __name__ == "__main__":
    main()