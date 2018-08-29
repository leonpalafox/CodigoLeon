# -*- coding: utf-8 -*-
import numpy as np
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
from sklearn.model_selection import train_test_split


baseDeDatosTe=pd.read_csv('globalterrorismdb_0617dist.csv',header=0)



ter=pd.DataFrame(baseDeDatosTe)
x=ter['region']
y=ter['iyear']

X_train, X_test, Y_train, Y_test = train_test_split(x,y)
print baseDeDatosTe