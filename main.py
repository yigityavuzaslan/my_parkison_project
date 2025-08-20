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


"""
#Cinsiyete Gore Motor UPDRS Skoru
df['sex'] = df['sex'].map({True: 'Kadın', False: 'Erkek'})
motor_updrs_means = df.groupby('sex')['motor_updrs'].mean()
plt.figure(figsize=(10,10))
plt.title("Cinsiyet ve Motor UPDRS Arasındaki İlişki")
sns.barplot(x=motor_updrs_means.index, y=motor_updrs_means.values, palette='viridis')
plt.xlabel("Cinsiyet")
plt.ylabel("Ortalama Motor UPDRS Skoru")
plt.show()
"""



"""
#Cinsiyete Gore Ort. Total UPDRS arasindaki İliskisi
df['sex'] = df['sex'].map({True: 'Kadın', False: 'Erkek'})
total_updrs_means = df.groupby('sex')['total_updrs'].mean()
plt.figure(figsize=(10,10))
plt.title("Cinsiyet ve Total UPDRS Arasındaki İlişki",color='red')
tablo=sns.barplot(x=total_updrs_means.index, y=total_updrs_means.values, palette="pastel") ##pastel,bright,deep,muted
tablo.bar_label(tablo.containers[0], fmt='%.2f')
tablo.bar_label(tablo.containers[1], fmt='%.2f')
plt.xlabel("Cinsiyet")
plt.ylabel("Ortalama Total UPDRS Skoru",color='black')
plt.show()
"""




"""
#ilk deneğin zamana göre Motor UPDRS Skoru Değişimi
first_subjects = df['subject'].unique()[:1]
df_filtered = df[df['subject'].isin(first_subjects)]


plt.figure(figsize=(10,10))
plt.title("Test Süresine Göre Motor UPDRS Skoru ")
plt.xlabel("Test Süresi(Gün)")
plt.ylabel("Motor UPDRS Skoru",color='black')
sns.lineplot(x="test_time",y="motor_updrs",data=df_filtered)
plt.show()
"""



"""
#Tüm denekler için ayrı ayrı alt grafikler
selected_subjects_for_facet = df['subject'].unique()[:9]
df_facet = df[df['subject'].isin(selected_subjects_for_facet)].copy()

#FacetGrid ile her denek icin ayri bir alt grafik
g = sns.FacetGrid(df_facet, col='subject', col_wrap=3, height=3, aspect=1.2, sharey=True)
g.map(sns.lineplot, 'test_time', 'motor_updrs', marker='o')
g.set_axis_labels("Süre (Gün)", "Motor UPDRS")
g.set_titles("Denek {col_name}")
g.tight_layout()  ##alt grafiklerin otomatik olarak çakışmasını engeller
plt.suptitle('Her Bir Denek İçin Motor UPDRS Zaman Serisi', y=1.001) #genel baslik
plt.show()
"""