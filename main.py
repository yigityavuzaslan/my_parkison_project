import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##Veri Kontrol(Null değer sayısı,describe..)
df=pd.read_csv('Parkinsons-Telemonitoring-ucirvine.csv')
print(df.head())

print(df.isnull().sum())  ##clear
print(df["test_time"].describe())
print(df.info())



