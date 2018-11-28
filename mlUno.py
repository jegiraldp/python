import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
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

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
names = ['Largo', 'Archo', 'Petalo_largo', 'Petalo_Ancho', 'clase']
dataset = pandas.read_csv(url, names=names)
# shape
print(dataset.shape)
# head
print(dataset.head(5))
# descriptions
#print(dataset.describe())
# class distribution
#print(dataset.groupby('clase').size())

# histograms
#dataset.hist()
#plt.show()
# scatter plot matrix
#scatter_matrix(dataset)
#plt.show()




print ("fin")