# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
sklearn : pour les predictions
numpy: Pour les calculs mathemetiques
matplotlib: graph
statsmodels: model stat
pandas : traiter les datasets
seaborn: visualisation

"""

#importation de package 

import statsmodels as stat
import seaborn as sbrn
import pandas as pds
import matplotlib.pyplot as mplt
import numpy as np

dtst = pds.read_csv("credit_immo.csv")
X = dtst.iloc[:,-9:-1].values
Y = dtst.iloc[:,-1].values

#data cleaning
from sklearn.preprocessing import Imputer
imptr = Imputer(missing_values= 'NaN', strategy ='mean', axis = 0)
imptr.fit(X[:,0:1])
imptr.fit(X[:,7:8])
X[:,0:1] = imptr.transform(X[:,0:1])
X[:,7:8] = imptr.transform(X[:,7:8])

#données categoriques

## Codage de la variable independant
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labEncre_X = LabelEncoder()
X[:,2] = labEncre_X.fit_transform(X[:,2])
X[:,5] = labEncre_X.fit_transform(X[:,5])
onehotEncr = OneHotEncoder(categorical_features=[2])
onehotEncr = OneHotEncoder(categorical_features=[5])
X = onehotEncr.fit_transform(X).toarray()

#varable dep 
labEncr_Y = LabelEncoder()
Y = labEncr_Y.fit_transform(Y)

# Fractionner l'ensemble de donnéé en train_test_split
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)


#Mise a echelle
from sklearn.preprocessing import normalize

X_train = normalize(X_train)
X_test = normalize(X_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
