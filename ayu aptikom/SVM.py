import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import svm


iris = pd.read_csv("Iris.csv")

y = iris.Species
x = iris.drop(['Species','Id'], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

clf = svm.SVC().fit(x_train, y_train)

y_predict = clf.predict(x_test)
print("accuracy : ", metrics.accuracy_score(y_test, y_predict))