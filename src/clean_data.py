import os
import pandas as pd

class DataCleaner:
    def __init__(self):
        self.gestures = self.get_gesture_list()
        self.dataset = pd.DataFrame()
        pass

    def get_gesture_list(self):
        gestures = []
        for file in os.listdir("dataset"):
            if '.csv' not in file:
                continue

            gestures.append(file[:-4])
        return gestures

    def combine_dataset(self, shuffle=True):
        dfs = []
        for file in self.gestures:
            df = pd.read_csv(f'dataset/{file}.csv', header=None)
            dfs.append(df)

        full_data = pd.concat(dfs)
        if shuffle:
            full_data = full_data.sample(frac=1)

        self.dataset = full_data
        return full_data

    # IN PROGRESS
    def balance_data(self, df):
        label_counts = df[0].value_counts()
        print(label_counts)
        print(label_counts.max() - label_counts.min(), "data entries would be lost")

        min_count = label_counts.min()
        df = df.sample(frac=1)

        return df
