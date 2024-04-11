from model import Model
import torch


class Trainer:
    def __init__(self, data_cleaner) -> None:
        # Base options and detector setup
        self.data_cleaner = data_cleaner
        self.gestures_list = self.data_cleaner.gestures

        print("All Gestures")
        print(self.gestures_list)
        dataset = self.data_cleaner.combine_dataset(shuffle=True)

        self.labels = dataset.reindex(columns=[0]).to_numpy().flatten()
        self.inputs = dataset.drop(0, axis=1).to_numpy()

        # print(len(self.inputs[0]), len(self.gestures_list))
        self.nn = Model(len(self.inputs[0]), len(self.gestures_list))

        self.epochs = 10
        pass

    def train(self, save=True):
        for _ in range(self.epochs):
            for i, ins in enumerate(self.inputs):
                label = torch.zeros(
                    [
                        len(self.gestures_list),
                    ]
                )
                label_index = self.gestures_list.index(self.labels[i])
                label[label_index] = 1.0
                self.nn.backprop(torch.Tensor(ins), torch.Tensor(label))

        if save:
            torch.save(self.nn.state_dict(), f"models/main_model.pt")


# Testing
# with open("testdata/palm.csv", "r") as f:
#     data = list(map(float, f.read().split(",")))
#     data = torch.Tensor(data)
#     out = nn.forward(data)
#     out = torch.argmax(out).item()
#     print(gestures_list[out])
