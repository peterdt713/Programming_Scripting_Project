# Peter Thornton, 14 Apr 18

# Initial Investigation into the Iris Data Set

# Below is adapted from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# The following aided in understanding Pandas: https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question1


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

# Creating a DataFrame for each Species
# Setosa
setosa = dataset[dataset['species']=='setosa']
print(setosa.describe())
setosa.to_csv('Data_Setosa_Breakdown.csv',sep=',')

# Versicolor
versicolor = dataset[dataset['species']=='versicolor']
print(versicolor.describe())
versicolor.to_csv('Data_Versicolor_Breakdown.csv',sep=',')

# Virginica
virginica = dataset[dataset['species']=='virginica']
print(virginica.describe())
virginica.to_csv('Data_Virginica_Breakdown.csv',sep=',')

#Setosa - Comparison of Petal Length vs Petal Width & Sepal Length vs Sepal width
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(17, 9))
setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal Comparasion Setosa', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion Setosa',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
plt.show()
plt.close()

#Versicolor - Comparison of Petal Length vs Petal Width & Sepal Length vs Sepal width
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(17, 9))
versicolor.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
versicolor.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal Comparasion Versicolor', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion Versicolor',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
plt.show()
plt.close()

#Virginica - Comparison of Petal Length vs Petal Width & Sepal Length vs Sepal width
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(17, 9))
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
virginica.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal Comparasion Virginica', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion Virginica',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
plt.show()
plt.close()

#Scatter plot of Sepal and Petal - All Species
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(21, 10))

setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter", ax=ax[0], label='virginica', color='g')

setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal_length", y="petal_width", kind="scatter", ax=ax[1], label='virginica', color='g')

ax[0].set(title='Sepal Comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
plt.show()
plt.close()

