# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:22:55 2024

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer


veriler = pd.read_csv('eksikveriler.csv')

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
Yas=veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)