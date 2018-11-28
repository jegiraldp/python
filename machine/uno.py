from sklearn import datasets

iris = datasets.load_iris()
print (iris.feature_names)
for v in iris.data[:,3]:
    if v > 2 and v < 3:
        print ("Iris-Versicolour --  petal width (cm): "+str(v)+"\n")
for i in iris.data[:, 1]:
    if i < 3:
        print("Iris Setosa --  sepal width in cm: " + str(i) + "\n")