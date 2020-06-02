#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 14:33:10 2018

@author: ravi
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt            

#importing the datasets
dataset= pd.read_csv('/home/ravi/Aiworkshop/day3/50_Startups.csv')

#separating dependent and independent variables
x= dataset.iloc[:,:4].values
y= dataset.iloc[:,4].values

#encoding the categorical values
from sklearn.preprocessing import LabelEncoder ,OneHotEncoder
lEncoder=LabelEncoder() #preprocesing data
x[:,3]=lEncoder.fit_transform(x[:,3])
ohEncoder = OneHotEncoder(categorical_features=[3])
x = ohEncoder.fit_transform(x).toarray()
x=x[:,1:]

#splitting data into train set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/5,random_state=0)

#sklearn provides linear regression intialise model and create model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
#prediction of testdata
y_predict =regressor.predict(x_test)

#building the optimal model using backward Elimination(consider small input data)
import statsmodels.formula.api as sm

x_zero=np.ones((50,1))
x=np.append(arr=x_zero,values=x,axis=1)

x_opt = x[:,[0,1,2,3,4,5]]
regressorOLS = sm.OLS(endog=y,exog=x_opt).fit()
regressorOLS.summary()

x_opt = x[:,[0,1,3,4,5]]
regressorOLS = sm.OLS(endog=y,exog=x_opt).fit()
regressorOLS.summary()

x_opt = x[:,[0,3,5]]
regressorOLS = sm.OLS(endog=y,exog=x_opt).fit()
regressorOLS.summary()

x_opt = x[:,[0,3]]
regressorOLS = sm.OLS(endog=y,exog=x_opt).fit()
regressorOLS.summary()

#------------------splitting 
from sklearn.cross_validation import train_test_split
x_train_opt,x_test_opt,y_train_opt,y_test_opt=train_test_split(x_opt,y,test_size=1/5,random_state=0)

regressor_new = LinearRegression()
regressor_new.fit(x_train_opt,y_train_opt)
#prediction of testdata
y_predict_new =regressor_new.predict(x_test_opt)
