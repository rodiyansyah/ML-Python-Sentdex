import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('spam.csv',encoding='latin-1')
for col in data.columns: 
    print(col) 