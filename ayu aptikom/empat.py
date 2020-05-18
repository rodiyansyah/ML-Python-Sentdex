import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
iris = pd.read_csv("Iris.csv")

sns.set_style('whitegrid')
sns.pairplot(iris, hue='Species', height=3)
plt.show()