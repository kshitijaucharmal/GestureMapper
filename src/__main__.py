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

# TODO: make it dynamic by setting these to folder names in data set folder
# hard coded gesture list
gestures_list = [
    'peace',
    'punch',
    'paper',
]

# Load image to classify
image = mp.Image.create_from_file("dataset/peace/image_1.jpg")

# Get detection result
detection_result = detector.detect(image)

# TODO: for training, load all images first, and then shuffle them

# get landmarks (these will act as inputs to model)
landmarks = detection_result.hand_landmarks[0]

# flatten to compress all landmarks into a single list
flattened_landmarks = []
for point in landmarks:
    flattened_landmarks.append(point.x)
    flattened_landmarks.append(point.y)
    flattened_landmarks.append(point.z)

# convert to torch tensor
flattened_landmarks = torch.Tensor(flattened_landmarks)

# Create model based on landmark size (63) and gestures size (3)
nn = Model(len(flattened_landmarks), len(gestures_list))

# Get output by feed forward
output = nn.forward(flattened_landmarks)

# print guess
gesture_guess = gestures_list[torch.argmax(output).item()]
print("This gesture is:", gesture_guess)
