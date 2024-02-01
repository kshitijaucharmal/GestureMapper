#!/usr/bin/env python

import cv2
import numpy as np
import os

# Initialize the camera
cap = cv2.VideoCapture(1)

# Initialize the frame count
frame_count = 0

# Loop over the frames
while True:
    class_label = input("Enter the class label: ")

    if class_label != 'exit':
        # Create a directory for the images
        directory = f"dataset/{class_label}"
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
            cv2.imwrite(f"{directory}/image_{frame_count}.jpg", frame)
            print("Recording frame:", frame_count)
            frame_count += 1

        # Check if the "q" key is pressed
        elif key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
