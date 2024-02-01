import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from pprint import pprint

from model import Model
import torch
import os

# Base options and detector setup
base_options = python.BaseOptions(model_asset_path='tasks/hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

# TODO: make it dynamic by setting these to file names in data set folder
# hard coded gesture list
gestures_list = [filename for filename in os.listdir('dataset')]



# Create model based on landmark size (63) and gestures size (3)
nn = Model(len(flattened_landmarks), len(gestures_list))

# Get output by feed forward
output = nn.forward(flattened_landmarks)

# print guess
for i, filename in enumerate(gestures_list):
    print(filename[:-4], output[i])
