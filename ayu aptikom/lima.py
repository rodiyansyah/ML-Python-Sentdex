import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px

iris = pd.read_csv("Iris.csv")

fig = px.scatter_3d(iris, x='SepalLengthCm', y='SepalWidthCm', z='PetalWidthCm', color='Species')
fig.show()