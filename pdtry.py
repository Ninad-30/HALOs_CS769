import pandas as pd

dataset = pd.read_csv("train.csv")

num_desirable = dataset[dataset['orig_score'] > 2].shape[0]
num_undesirable = dataset[dataset['orig_score'] <= 2].shape[0]

print(dataset.isna().sum())
# print(num_desirable, num_undesirable, num_desirable/num_undesirable)


