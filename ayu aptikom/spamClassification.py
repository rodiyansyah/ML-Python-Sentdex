import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('spam.csv',encoding='latin-1')
data.columns = ['v1','v2','v3','v4','v5']
data = data.rename(columns = {'v1': 'label', 'v2': 'text'})


spam_count = data.groupby('label').count()
plt.bar(spam_count.index.values, spam_count['text'])
plt.xlabel('spam label')
plt.ylabel('Number of text')
plt.show()