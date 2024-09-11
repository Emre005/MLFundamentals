# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:36:04 2024

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


veriler = pd.read_csv('satislar.csv')
aylar = veriler[['Aylar']]
satislar = veriler[['Satislar']]

satislar2 = veriler.iloc[:,:1].values

x_train, x_test,y_train,y_test = train_test_split(aylar, satislar, test_size=0.33,random_state=0)

sc=StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)