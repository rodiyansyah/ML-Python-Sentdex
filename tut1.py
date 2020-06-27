import pandas as pd
import math
import datetime
import numpy as np
from sklearn import preprocessing 
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = pd.read_csv('data_stock.csv',index_col=0)

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume', ]]

# preprocessing
df['HL_PCT'] =(df['Adj. High']-df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_ch'] =(df['Adj. Close']-df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close','HL_PCT','PCT_ch', 'Adj. Volume']]
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)
forecast_out = int(math.ceil(0.01*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)
x = np.array(df.drop(['label'],1))
x = preprocessing.scale(x)
x = x[:-forecast_out]
x_lately = x[-forecast_out:]
df.dropna(inplace=True)
y =np.array(df['label'])
y = np.array(df['label'])

#pembagian data training dan testing
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

#proses utama regresi linear
clf = LinearRegression(n_jobs=10)
clf.fit(x_train, y_train)

#perhitungan akurasi
accuracy = clf.score(x_test, y_test)
print(accuracy)

#memprediksi data baru
forecast_set = clf.predict(x_lately);

#proses cetak grafik
print(forecast_set, accuracy, forecast_out)
df['Forecast'] = np.nan
str_last_date = df.iloc[-1].name
last_date = datetime.datetime.strptime(str_last_date, '%Y-%m-%d')
print('last date :',last_date)
last_unix =last_date.timestamp()
print('last unix :',last_unix)
one_day = 86400
next_unix = last_unix+one_day
for i in forecast_set:
	next_date = datetime.datetime.fromtimestamp(next_unix)
	next_unix += one_day
	df.loc[next_date] = [np.nan for __ in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


