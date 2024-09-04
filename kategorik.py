# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:40:21 2024

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

veriler = pd.read_csv('eksikveriler.csv')

ulke = veriler.iloc[:,0:1].values
Yas=veriler.iloc[:,1:4].values
print(ulke)

le = preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)
ohe=preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

print(list(range(22)))
sonuc = pd.DataFrame(data = ulke, index=range(22),columns=['fr','tr','us'])
print(sonuc)

sonuc2 = pd.DataFrame(data = Yas,index=range(22),columns=['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3=pd.DataFrame(data=cinsiyet,index=range(22),columns=['cinsiyet'])
print(sonuc)
s=pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2= pd.concat([s,sonuc3],axis=1)
print(s2)

x_train, x_test,y_train,y_test = train_test_split(s, sonuc3, test_size=0.33,random_state=0)
