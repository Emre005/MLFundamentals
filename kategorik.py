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

veriler = pd.read_csv('eksikveriler.csv')

ulke = veriler.iloc[:,0:1].values
print(ulke)

le = preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)
ohe=preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)