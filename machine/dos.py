from sklearn import datasets
import pandas as pd

sk_iris = datasets.load_iris()
#print (sk_iris.data)
iris = pd.DataFrame(data=sk_iris.data, columns=sk_iris.feature_names)
iris['labels'] = pd.Categorical.from_codes(sk_iris.target, sk_iris.target_names)
#print (iris['labels'])
for i in range(0,len(iris['labels'])):
    if(iris['labels'][i]=='virginica'):
        print (iris['labels'][i])