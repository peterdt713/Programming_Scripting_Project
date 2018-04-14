# Peter Thornton, 14 Apr 18

# Initial Investigation into the Iris Data Set

# Below is adapted from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

#Importing Package 
import sys
import numpy
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import warnings

#Import Iris Data set into Pandas
raw_data="iris.data.csv"
dataset = pandas.read_csv(raw_data)

#Count the size of each Species Size
print(dataset.groupby('species').size())

# Describe the Data set
print(dataset.describe())

# Saving Data to a CSV file
data_full = dataset.describe()
data_full.to_csv('Data_Set_Breakdown.csv',sep=',')