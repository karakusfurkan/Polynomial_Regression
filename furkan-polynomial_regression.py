#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:03:32 2020

@author: furkan
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%%
# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
#%%
X = dataset.iloc[:, 1:-1].values #should be matrix (10,1) 
y = dataset.iloc[:, 2].values    #should be vector (10,)#variable explorer-->
#%%
#because of data is so little, we will use all data to train.
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
#%%
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
#%%
#Visualization with simple linear regression
plt.scatter(X,y, color = 'orange')
plt.plot(X, lin_reg.predict(X), color = 'green')
plt.title('Truth or Bluff(Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
#%%
#Visualization with polynomial regression (degree = 4)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1)) #for curve... 10 piece --> 100
plt.scatter(X,y, color = 'orange')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'green')
plt.title('Truth or Bluff(Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')

 #%%
 #Predict 6.5
 #with linear regression
 lin_reg.predict([[6.5]])
 #%%
 #with polynomial regression
 lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
 
 