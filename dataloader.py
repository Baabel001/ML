import chardet
import pandas as pd


path = "C:\\Users\\LENOVO\\Desktop\\ML_project\\ML\\input\\Train.csv"

with open(path, 'rb') as f:
    result = chardet.detect(f.read())

data = pd.read_csv(path, delimiter = ",",decimal = ".", encoding = result['encoding'])

