# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:29:10 2024

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler = pd.read_csv('veriler.csv')

boy = veriler[['boy']]
print(boy)