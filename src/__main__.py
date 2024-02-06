import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from pprint import pprint

from model import Model
from clean_data import DataCleaner
import torch
import os
import pandas as pd

# Base options and detector setup
base_options = python.BaseOptions(model_asset_path='tasks/hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

data_cleaner = DataCleaner()

# hard coded gesture list
gestures_list = data_cleaner.gestures

dataset = data_cleaner.combine_dataset(shuffle=True)

labels = dataset.reindex(columns = [0]).to_numpy().flatten()
inputs = dataset.drop(0, axis=1).to_numpy()

nn = Model(len(inputs[0]), len(gestures_list))
epocs = 30

for _ in range(epocs):
    for i, ins in enumerate(inputs):
        label = torch.zeros([len(gestures_list),])
        label_index = gestures_list.index(labels[i])
        label[label_index] = 1.
        nn.backprop(torch.Tensor(ins), torch.Tensor(label))
