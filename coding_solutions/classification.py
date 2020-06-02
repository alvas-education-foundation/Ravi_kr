#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 22:44:27 2018

@author: cse_a1
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing datasets
dataset = pd.read_csv('/home/ravi/Aiworkshop/day4/Social_Network_Ads.csv')
#storing age and salary in x
x=dataset.iloc[:,[2,3]].values
#storing purchased data in y
y=dataset.iloc[:,4].values

#splitting to test and train data
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)

#standardising the data 
from sklearn.preprocessing import StandardScaler
sScaler = StandardScaler()
x_train = sScaler.fit_transform(x_train)
x_test = sScaler.fit_transform(x_test)

#fitting the data
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)

#prediction
y_predict = classifier.predict(x_test)

from sklearn.externals import joblib
joblib.dump(classifier,'classifier_model.save')

joblib.dump(sScaler,'Std_scaler.save')





