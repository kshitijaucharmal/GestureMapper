import cv2
import os
import numpy as np
import pandas as pd

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

from model import Model
from clean_data import DataCleaner
from train import Trainer
import torch
import time

MARGIN = 10
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)  # vibrant green


class Detector:

    def __init__(self, recording=False, train=True):
        self.data_cleaner = DataCleaner()

        # Base options and detector setup
        self.base_options = python.BaseOptions(
            model_asset_path="tasks/hand_landmarker.task"
        )
        self.options = vision.HandLandmarkerOptions(
            base_options=self.base_options, num_hands=1
        )
        self.detector = vision.HandLandmarker.create_from_options(self.options)
        self.recording = recording  # Initialize the camera
        self.cap = cv2.VideoCapture(0)
        self.gestures_list = self.data_cleaner.gestures

        if train:
            trainer = Trainer(self.data_cleaner)
            trainer.train()
            self.nn = trainer.nn
        else:
            self.nn = Model(63, len(self.gestures_list))
            self.nn.load_state_dict(torch.load("models/main_model.pt"))

        print("Initialization Done")
        print("Start Showing gestures to the camera..")

        self.detected_gesture = -1
        self.time_thres = 2
        self.time_ctr = 0
        self.start_time = time.time()
        pass

    def draw_landmarks_on_image(self, rgb_image, detection_result):
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

    def main_loop(self):
        # Loop over the frames
        while True:
            # if self.recording:
            #     class_name = self.set_class_name()

            ret, frame = self.cap.read()

            if not ret:
                break

            # Detect by default
            self.detect(frame)

            key = cv2.waitKey(1)

            # Check if the "q" key is pressed
            if key == ord("q"):
                break

    def set_class_name(self):
        class_label = input("Enter the class label: ")

        if class_label != "exit":
            # Create a directory for the images
            directory = f"dataset"
            os.makedirs(directory, exist_ok=True)
            return class_label
        else:
            return ""

    def detect(self, frame):
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        self.detection_result = self.detector.detect(image)

        if self.detection_result.handedness != []:
            landmarks = self.detection_result.hand_landmarks[0]

            flattened_landmarks = []
            for point in landmarks:
                flattened_landmarks.append(point.x)
                flattened_landmarks.append(point.y)
                flattened_landmarks.append(point.z)

            out = self.nn.forward(torch.Tensor(flattened_landmarks))
            out = torch.argmax(out).item()
            print(self.gestures_list[out])

            if self.time_ctr > self.time_thres:
                self.time_ctr = 0
                self.start_time = time.time()

                self.perform_action(out)

                # print(
                #     self.time_thres,
                #     "seconds done,",
                #     self.gestures_list[out],
                #     "gesture detected",
                # )

                pass
            else:
                self.time_ctr = time.time() - self.start_time
                if self.detected_gesture != out:
                    # Gesture changed
                    self.start_time = time.time()
                    self.time_ctr = 0

            # Set detected_gesture
            self.detected_gesture = out

            # Show
            self.show(frame, True)
            pass

    def perform_action(self, gesture_id):
        df = pd.read_csv("data.csv")
        print(df)
        print("Action to be taken ", df.loc[gesture_id])
        pass

    def show(self, frame, annotated=False):
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        if annotated:
            detection_result = self.detector.detect(image)
            annotated_image = self.draw_landmarks_on_image(
                image.numpy_view(), detection_result
            )
            frame = annotated_image
        cv2.imshow("Frame", frame)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
