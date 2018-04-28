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
import scipy
import sklearn
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

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

# The below code is adapted from the following: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Box and Whisker plots - All species
# Q: Print Box & Whisker plot?
if input("Would you like to view a Box & Whisker plot of the full dataset? (Y/N): ") == "Y":
    dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    plt.show()
    plt.close()

# histogram - All species
# Q: Print Histogram?
if input("Would you like to view a histogram of the full dataset? (Y/N): ") == "Y":
    dataset.hist()
    plt.show()
    plt.close()

# scatter plot matrix - All species
# Q: Print Scatter Matrix?
if input("Would you like to view a scatter matrix of the full dataset? (Y/N): ") == "Y":
    scatter_matrix(dataset)
    plt.show()

# Q: Machine Learning?
if input("Would you like to build and test a machine learning model? (Y/N): ") == "Y":
    # Split-out validation dataset
    print("Splitting the data into 0.8 for learning and 0.2 for testing...")
    array = dataset.values
    X = array[:,0:4]
    Y = array[:,4]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'
    
    print("Creating 5 models,'LR' LogisticRegression, 'LDA' LinearDiscriminantAnalysis, 'KNN' KNeighborsClassifier, 'CART' DecisionTreeClassifier, 'NB' GaussianNB, 'SVM' SVC ...")
    # Spot Check Algorithms
    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    # evaluate each model in turn
    results = []
    names = []
    # Q: Print Evaluation?
    if input("Would you like view the evaluation of each model? (Y/N): ") == "Y":
        for name, model in models:
	        kfold = model_selection.KFold(n_splits=10, random_state=seed)
	        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	        results.append(cv_results)
	        names.append(name)
	        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	        print(msg)
    
    # Q: Print Evaluation #2?
    if input("Would you like view a box and whisker plot of each model? (Y/N): ") == "Y":
        # Compare Algorithms
        fig = plt.figure()
        fig.suptitle('Algorithm Comparison')
        ax = fig.add_subplot(111)
        plt.boxplot(results)
        ax.set_xticklabels(names)
        plt.show()
    
    print("SVM is the most accurate...") # According to the tutorial KNN is the most accurate. This could not be replicated. The below model is based on what was noted as the most accurate.
    # Q: Make Predictions?
    if input("Would you like to Make Predictions using the remaining 0.2 of the data? (Y/N): ") == "Y":
        # Make predictions on validation dataset
        SVM = SVC()
        SVM.fit(X_train, Y_train)
        predictions = SVM.predict(X_validation)
        print(accuracy_score(Y_validation, predictions))
        print(confusion_matrix(Y_validation, predictions))
        print(classification_report(Y_validation, predictions))