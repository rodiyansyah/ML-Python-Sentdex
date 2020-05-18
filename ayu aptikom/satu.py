from sklearn import datasets
iris = datasets.load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0:10]