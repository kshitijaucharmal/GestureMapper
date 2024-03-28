#!/usr/bin/env python

import cv2
import os
import numpy as np

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

from model import Model
import torch

MARGIN = 10
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)  # vibrant green


# Base options and detector setup
base_options = python.BaseOptions(model_asset_path="tasks/hand_landmarker.task")
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

# Initialize the camera
cap = cv2.VideoCapture(0)


def draw_landmarks_on_image(rgb_image, detection_result):
    hand_landmarks_list = detection_result.hand_landmarks
    handedness_list = detection_result.handedness
    annotated_image = np.copy(rgb_image)

    # Loop through the detected hands to visualize.
    for idx in range(len(hand_landmarks_list)):
        hand_landmarks = hand_landmarks_list[idx]
        handedness = handedness_list[idx]

        # Draw the hand landmarks.
        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend(
            [
                landmark_pb2.NormalizedLandmark(
                    x=landmark.x, y=landmark.y, z=landmark.z
                )
                for landmark in hand_landmarks
            ]
        )
        solutions.drawing_utils.draw_landmarks(
            annotated_image,
            hand_landmarks_proto,
            solutions.hands.HAND_CONNECTIONS,
            solutions.drawing_styles.get_default_hand_landmarks_style(),
            solutions.drawing_styles.get_default_hand_connections_style(),
        )

        # Get the top left corner of the detected hand's bounding box.
        height, width, _ = annotated_image.shape
        x_coordinates = [landmark.x for landmark in hand_landmarks]
        y_coordinates = [landmark.y for landmark in hand_landmarks]
        text_x = int(min(x_coordinates) * width)
        text_y = int(min(y_coordinates) * height) - MARGIN

        # Draw handedness (left or right hand) on the image.
        cv2.putText(
            annotated_image,
            f"{handedness[0].category_name}",
            (text_x, text_y),
            cv2.FONT_HERSHEY_DUPLEX,
            FONT_SIZE,
            HANDEDNESS_TEXT_COLOR,
            FONT_THICKNESS,
            cv2.LINE_AA,
        )

    return annotated_image


# Initialize the frame count
frame_count = 0

nn = Model(63, 5)
nn.load_state_dict(torch.load(f"models/main_model.pt"))
gestures_list = ["palm", "palm_left", "peace", "thumbsdown_left", "thumbsup_right"]

# Loop over the frames
while True:
    class_label = input("Enter the class label: ")

    if class_label != "exit":
        # Create a directory for the images
        directory = f"dataset"
        os.makedirs(directory, exist_ok=True)
    else:
        break

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Check if the "r" key is pressed
        key = cv2.waitKey(1)
        if key == ord("r"):
            image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            detection_result = detector.detect(image, num_hands=1)

            if detection_result.handedness != []:

                flattened_landmarks = []
                for point in landmarks:
                    flattened_landmarks.append(point.x)
                    flattened_landmarks.append(point.y)
                    flattened_landmarks.append(point.z)
                with open(f"dataset/{class_label}.csv", "a") as f:
                    f.write(
                        f"{class_label},"
                        + ",".join(str(lm) for lm in flattened_landmarks)
                        + "\n"
                    )

                print("Recording frame:", frame_count)
                frame_count += 1

        # Prediction images
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        detection_result = detector.detect(image)
        annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
        cv2.imshow("Frame", annotated_image)

        if detection_result.handedness != []:
            landmarks = detection_result.hand_landmarks[0]
            landmarks = detection_result.hand_landmarks[0]

            flattened_landmarks = []
            for point in landmarks:
                flattened_landmarks.append(point.x)
                flattened_landmarks.append(point.y)
                flattened_landmarks.append(point.z)

            out = nn.forward(torch.Tensor(flattened_landmarks))
            out = torch.argmax(out).item()
            print(gestures_list[out])

        # Check if the "q" key is pressed
        if key == ord("q"):
            break


cap.release()
cv2.destroyAllWindows()
