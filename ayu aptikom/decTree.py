import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

iris = pd.read_csv("Iris.csv")

y = iris.Species
x = iris.drop(['Species','Id'], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

clf = DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)


y_predict = clf.predict(x_test)
print("accuracy : ", metrics.accuracy_score(y_test, y_predict))

cm = metrics.confusion_matrix(y_test, y_predict)
cm_display = metrics.ConfusionMatrixDisplay(cm, display_labels=cm).plot()
plt.show()