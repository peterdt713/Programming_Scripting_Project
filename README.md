# Programming_Scripting_Project
This project is comprised of research into the Fisher’s Iris data set.


# Project Statement
The project initially is comprised of research in the Iris Data Set. This will include, but is not limited to, the original publication of the data set, the development of the data set as historical significant, current methods utilised to analyse and visualize the various characteristics of the data.

^ Re-edit: Update throughout project i.e. research findings

# Initial Research
Ronald Fisher, a British statistician and biologist, first introduced the Iris Data set in 1936 in an article published in the peer-reviewed journal *Annals of Human Genetics*. [1] The article, *The use of multiple measurements in taxonomic problems*, details the measurements of three species of Iris flower that were growing within the same colony. The four measurements taken, for fifty of each the species, were the Sepal length, Sepal width, Petal length and Petal width. These measurements, which can be seen in table I of the article, would become the well known and commonly used Iris Data set. The three species were the iris setosa, iris versicolor and iris virginica.

![](Iris_Images.png)
<b>Image 1:</b> Three species of Iris flower utilized in the data set. [2]

The article continues to describe the arithmetical produce utilized in the analysis of the data. Beginning with the observed means and their differences for two of the species before specifying more in-depth statistical analysis. [1]

# Python Research
Upon beginning to research the methods into how to visualize the Iris Data set, Pandas Dataframes was discovered. Several tools are available to aid in the understanding and use. 

Steps:
* Downloaded the Iris Data Set and subsequently imported the data into pandas.
~~~~
#Import Iris Data set into Pandas
raw_data="iris.data.csv"
dataset = pandas.read_csv(raw_data)
~~~~
* Verified that the sample size of each species was 50. As in accordance with the background research.
* *paste code*
* Using dataset.describe, *insert reference*,  to calculate the Count, Mean, STD, Min & Max and the percentiles of the dataset. After this was visualized using the print function and finally this was saved into a CSV file.
* *paste code & dataset.describe*
* This was repeated for all three species.
* *paste code & dataset.describe*
* Scatterplots were created for all three species & a combined scatter plot. Subsequently saved.
* *paste code & Scatterplots & describe trends noted*


# References **Edit to Havard Style*

[1] https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x

[2] http://mirlab.org/jang/books/dcpr/dataSetIris.asp?title=2-2%20Iris%20Dataset

[3] https://pandas.pydata.org/pandas-docs/stable/visualization.html

[4] https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question1

[5] https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

[6] https://en.support.wordpress.com/markdown-quick-reference/
