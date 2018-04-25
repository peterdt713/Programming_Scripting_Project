# Peter Thornton, 14 Apr 18

# Initial Investigation into the Iris Data Set

# Below is adapted from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# The following site details a machine learning project in a step-by-step format. This was followed. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# The following aided in understanding Pandas: https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question1


#Importing Package 
import sys
import numpy
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import warnings
import os

#Import Iris Data set into Pandas
raw_data="iris.data.csv"
dataset = pandas.read_csv(raw_data)

# Q: Print Basic Data?
if input("Would you like to view a basic descriptive statistics for the full dataset? (Y/N): ") == "Y":
    #Count the size of each Species
    print(dataset.groupby('species').size())

    # Describe the Data set
    print(dataset.describe())

# Saving Data to a CSV file
data_full = dataset.describe()
# Check is CSV file already exists (https://www.cyberciti.biz/faq/python-file-exists-examples/)
if ( not os.path.isfile('Data_Set_Breakdown.csv')):
    data_full.to_csv('Data_Set_Breakdown.csv',sep=',')


# Creating a DataFrame for each Species
# Setosa
setosa = dataset[dataset['species']=='setosa']
data_setosa = setosa.describe()
# Q: Print Basic Data?
if input("Would you like to view a basic descriptive statistics for the setosa dataset? (Y/N): ") == "Y":
    print(setosa.describe())
# Check is CSV file already exists (https://www.cyberciti.biz/faq/python-file-exists-examples/)
if ( not os.path.isfile('Data_Setosa_Breakdown.csv')):
    data_setosa.to_csv('Data_Setosa_Breakdown.csv',sep=',')

# Versicolor
versicolor = dataset[dataset['species']=='versicolor']
data_versicolor = versicolor.describe()
# Q: Print Basic Data?
if input("Would you like to view a basic descriptive statistics for the versicolor dataset? (Y/N): ") == "Y":
    print(versicolor.describe())
# Check is CSV file already exists (https://www.cyberciti.biz/faq/python-file-exists-examples/)
if ( not os.path.isfile('Data_Versicolor_Breakdown.csv')):
    data_versicolor.to_csv('Data_Versicolor_Breakdown.csv',sep=',')

# Virginica
virginica = dataset[dataset['species']=='virginica']
data_virginica = virginica.describe()
# Q: Print Basic Data?
if input("Would you like to view a basic descriptive statistics for the virginica dataset? (Y/N): ") == "Y":
    print(virginica.describe())
# Check is CSV file already exists (https://www.cyberciti.biz/faq/python-file-exists-examples/)
if ( not os.path.isfile('Data_Virginica_Breakdown.csv')):
    data_virginica.to_csv('Data_Virginica_Breakdown.csv',sep=',')

#Setosa - Comparison of Petal Length vs Petal Width & Sepal Length vs Sepal width
# Q: Print Scatterplot?
if input("Would you like to view a scatterplot of the setosa dataset? (Y/N): ") == "Y":
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
# Q: Print Scatterplot?
if input("Would you like to view a scatterplot of the versicolor dataset? (Y/N): ") == "Y":
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
# Q: Print Scatterplot?
if input("Would you like to view a scatterplot of the virginica dataset? (Y/N): ") == "Y":
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
# Q: Print Scatterplot?
if input("Would you like to view a scatterplot of the full dataset? (Y/N): ") == "Y":
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

