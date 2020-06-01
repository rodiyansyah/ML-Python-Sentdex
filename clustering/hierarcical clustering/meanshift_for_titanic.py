import numpy as np
from sklearn.cluster import MeanShift, KMeans
from sklearn import preprocessing
from sklearn.model_selection import cross_validate
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('titanic.xls')
pd.set_option('display.max_columns', None)
#print(df.head())
original_df = pd.DataFrame.copy(df)

df.drop(['body', 'name'], 1, inplace=True)
df.convert_dtypes(convert_integer=True)
df.fillna(0, inplace=True)

def handle_non_numerical_data(df):
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1

            df[column] = list(map(convert_to_int, df[column]))

    return df

df = handle_non_numerical_data(df)
df.drop(['ticket','home.dest'],1,inplace=True)
X = np.array(df.drop(['survived'], 1).astype(float))
X = preprocessing.scale(X)
y = np.array(df['survived'])

clf = MeanShift()
clf.fit(X)

labels = clf.labels_
cluster_centers = clf.cluster_centers_

original_df['cluster_group'] = np.nan

for i in range(len(X)):
    original_df['cluster_group'].iloc[i]= labels[i]

n_clusters_= len(np.unique(labels))
survival_rates = {}

for i in range(n_clusters_):
    temp_df = original_df[(original_df['cluster_group'] == float(i))]
    # print(temp_df.head())
    survival_cluster = temp_df[(temp_df['survived'] == 1)]
    survival_rate = len(survival_cluster) / len(temp_df)
    # print(i,survival_rate)
    survival_rates[i] = survival_rate

print(survival_rates)
print(original_df[ (original_df['cluster_group']==1) ])
print(original_df[ (original_df['cluster_group']==0) ].describe())
print(original_df[ (original_df['cluster_group']==2) ].describe())