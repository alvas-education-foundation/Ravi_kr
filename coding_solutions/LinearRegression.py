# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
salary imortng simple  program
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#reading data
datset=pd.read_csv('/home/ravi/Aiworkshop/day3/Salary_Data.csv')
x=datset.iloc[:,:-1].values
y=datset.iloc[:,1].values

#splitting data 
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)

#intialise and create model   
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#prediction
y_predict =regressor.predict(x_test)

#dat representatio using graph matlib
y_predict = regressor.predict(x_test)

#train data #graph in new window using %matplotlib
%matplotlib auto 
plt.figure(1)
plt.subplot(221)
plt.scatter(x_train,y_train,color='red')
plt.xlabel('Years of Exp')
plt.ylabel('salary')
#graph of regresser
plt.plot(x_train,regressor.predict(x_train),color='blue')

plt.subplot(222)
plt.scatter(x_test,y_test,color='green')
plt.xlabel('Years of Exp')
plt.ylabel('salary')
#graph of regresser
plt.plot(x_test,regressor.predict(x_test),color='blue')

plt.subplot(223)
plt.scatter(x_test,y_test,color='green')
plt.scatter(x_train,y_train,color='red')
plt.xlabel('Years of Exp')
plt.ylabel('salary')
#graph of regresser
#plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.plot(x_test,regressor.predict(x_test),color='red')
plt.show()
