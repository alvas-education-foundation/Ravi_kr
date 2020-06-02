#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:34:27 2018

@author: ravi
"""


#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing datasets
dataset = pd.read_csv('Social_Network_Ads.csv')
#storing age and salary in x
x=dataset.iloc[:,[2,3]].values
#storing purchased data in y
y=dataset.iloc[:,4].values

#splitting to test and train data
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_stat
from sklearn.externals import jobhlibe=0)

scaler=joblib.load('Std_scaler.save')
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_tranform(x_test)

model = joblib.load(classifier_model.save')
y_predict = model.predict(x_test)
