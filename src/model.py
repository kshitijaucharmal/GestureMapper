import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self, inodes, onodes):
        super().__init__()
        self.layer1 = nn.Linear(inodes, 16)
        self.layer2 = nn.Linear(16, 16)
        self.layer3 = nn.Linear(16, onodes)
        pass

    def forward(self, x):
        x = self.layer1(x)
        x = F.relu(x)
        x = self.layer2(x)
        x = F.relu(x)
        x = self.layer3(x)
        x = F.tanh(x)
        return x

    def backprop(self, x, y):
        y_pred = self.forward(x)

        loss = self.loss_function(y_pred, y)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
