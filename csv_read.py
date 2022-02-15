import pandas as pd
#import numpy as np


dir = "C:/Users/sucheol/Desktop/archive/"
train_csv = pd.read_csv(dir + 'train.csv')
test_cst = pd.read_csv(dir + "test.csv")

print(train_csv.dropna())

