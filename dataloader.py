import chardet
import pandas as pd

with open('Train.csv', 'rb') as f:
    result = chardet.detect(f.read())

data = pd.read_csv('Train.csv', delimiter = ",",decimal = ".", encoding = result['encoding'])