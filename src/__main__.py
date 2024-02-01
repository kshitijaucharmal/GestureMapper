import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from pprint import pprint

from model import Model
import torch
import os
import pandas as pd

# Base options and detector setup
base_options = python.BaseOptions(model_asset_path='tasks/hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

# hard coded gesture list
gestures_list = {
        'peace':0,
        'thumbsdown':1,
        'thumbsup':2,
    }

dataset = pd.read_csv("dataset/dataset.csv", header=None).sample(frac=1)

labels = dataset.reindex(columns = [0]).to_numpy().flatten()
inputs = dataset.drop(0, axis=1).to_numpy()

nn = Model(len(inputs[0]), len(gestures_list))
epocs = 30

for _ in range(epocs):
    for i, ins in enumerate(inputs):
        label = torch.tensor([0., 0., 0.])
        label_index = gestures_list[labels[i]]
        label[label_index] = 1.
        nn.backprop(torch.Tensor(ins), torch.Tensor(label))
