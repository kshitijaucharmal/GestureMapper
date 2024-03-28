import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self, inodes, onodes):
        super().__init__()
        n_layer1 = 24
        n_layer2 = 16

        self.layer1 = nn.Linear(inodes, n_layer1)
        self.layer2 = nn.Linear(n_layer1, n_layer2)
        self.layer3 = nn.Linear(n_layer2, onodes)
        self.loss_function = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.SGD(self.parameters(), lr=0.05)
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
        print('Loss:', loss.item())
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
