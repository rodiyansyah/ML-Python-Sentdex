import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
iris = pd.read_csv("Iris.csv")
print(iris.describe())

plt.plot(iris["Species"])
plt.show()
