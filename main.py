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


#Yas ve Motor UPDRS Arasindaki iliski
plt.figure(figsize=(15,15))
plt.title("Yaş ve motor UPDRS Arasındaki İlişki")
sns.barplot(x="age",y="motor_updrs",data=df)
plt.xlabel("Yas")
plt.ylabel("Motor UPDRS Siddeti")
plt.show()

