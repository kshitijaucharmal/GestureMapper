from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from model import Model
from clean_data import DataCleaner
import torch

# Base options and detector setup
base_options = python.BaseOptions(model_asset_path='tasks/hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

data_cleaner = DataCleaner()

# hard coded gesture list
gestures_list = data_cleaner.gestures

print(gestures_list)
dataset = data_cleaner.combine_dataset(shuffle=True)

labels = dataset.reindex(columns = [0]).to_numpy().flatten()
inputs = dataset.drop(0, axis=1).to_numpy()

print(len(inputs[0]), len(gestures_list))
nn = Model(len(inputs[0]), len(gestures_list))
epochs = 10

# Load Model
# nn.load_state_dict(torch.load('model'))

# Traning
for _ in range(epochs):
    for i, ins in enumerate(inputs):
        label = torch.zeros([len(gestures_list),])
        label_index = gestures_list.index(labels[i])
        label[label_index] = 1.
        nn.backprop(torch.Tensor(ins), torch.Tensor(label))

# torch.save(nn.state_dict(), f'models/main_model.pt')

# Testing
with open('testdata/palm.csv', 'r') as f:
    data = list(map(float, f.read().split(',')))
    data = torch.Tensor(data)
    out = nn.forward(data)
    out = torch.argmax(out).item()
    print(gestures_list[out])
