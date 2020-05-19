import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
iris = pd.read_csv("Iris.csv")

#sns.FacetGrid(iris, hue="Species", height=5).map(plt.scatter, 'SepalLengthCm', 'SepalWidthCm').add_legend()
sns.FacetGrid(iris, hue="Species", height=5).map(plt.scatter, 'PetalLengthCm', 'PetalWidthCm').add_legend()
plt.show()