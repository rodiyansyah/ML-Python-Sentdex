import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px

from sklearn.model_selection import train_test_split

iris = pd.read_csv("Iris.csv")

y = iris.Species
x = iris.drop(['Species','Id'], axis=1)
print(x.describe())
print(y.describe())

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)