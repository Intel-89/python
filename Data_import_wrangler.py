# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:10:00 2020

@author: W10_Desktop
"""
#------------------------------------------------------------------------------------------------------------
import numpy as np   # numpy
import pandas as pd  # pandas
import matplotlib.pyplot as plt
import seaborn as sns# seaborn

#%matplotlib inline   # python inline magic function # "%matplotlib notebook:" will lead to interactive plots embedded within the notebook, you can zoom and resize the figure

#import pdpipe as pdp # Easy pipelines for pandas DataFrames # https://pdpipe.github.io/pdpipe/doc/pdpipe/
#------------------------------------------------------------------------------------------------------------

oDf = pd.read_csv('Datasets/anime-recommendations-database/anime.csv')

#print("Data shape: ", oDf.shape)  # rows x columns amount

#print("Feature variable types: ", oDf.info()) # types of variables per column

#print("Stats over data: ", oDf.describe()) # stats based on dataframe

#print("First records from data are: ", oDf.head()) # rows x columns amount

#print(oDf.columns.value_counts())

for (colName, colData) in oDf.iteritems(): # oDf.nunique(axis=1) # this line will return same as loop but with indexs instead of columns names
   print('Colunm Name      : ', colName)
   print('Column U. Values : ', len(colData.unique())) # N/A not included on results
   
oDf.plot(kind='hist',x='type')
plt.show()


oDf.plot.