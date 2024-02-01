#!/usr/bin/env python

import cv2
import numpy as np
import os

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from pprint import pprint

from model import Model
import torch
# Base options and detector setup
base_options = python.BaseOptions(model_asset_path='tasks/hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)


# Initialize the camera
cap = cv2.VideoCapture(1)

# Initialize the frame count
frame_count = 0

# Loop over the frames
while True:
    class_label = input("Enter the class label: ")

    if class_label != 'exit':
        # Create a directory for the images
        directory = f"dataset"
        os.makedirs(directory, exist_ok=True)
    else:
        break

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Frame", gray)

        # Check if the "r" key is pressed
        key = cv2.waitKey(1)
        if key == ord("r"):
            image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            detection_result = detector.detect(image)
            if detection_result.handedness != []:
                landmarks = detection_result.hand_landmarks[0]

                flattened_landmarks = []
                for point in landmarks:
                    flattened_landmarks.append(point.x)
                    flattened_landmarks.append(point.y)
                    flattened_landmarks.append(point.z)
                with open(f'dataset/{class_label}.csv', 'a') as f:
                    f.write(','.join(str(lm) for lm in flattened_landmarks) + '\n')

                print("Recording frame:", frame_count)
                frame_count += 1

        # Check if the "q" key is pressed
        elif key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
