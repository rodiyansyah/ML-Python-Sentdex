import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing 
from sklearn.model_selection import cross_validate
from sklearn import svm
from sklearn.linear_model import LinearRegression



quandl.ApiConfig.api_key = "WLJMuhZbyKPneqQNBEAZ"
df = quandl.get("WIKI/GOOGL")

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume', ]]

df['HL_PCT'] =(df['Adj. High']-df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_ch'] =(df['Adj. Close']-df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','PCT_ch', 'Adj. Volume']]

forecast_col = 'Adj. Close'

df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

x = np.array(df.drop(['label'],1))
y =np.array(df['label'])

x = preprocessing.scale(x)

#x = x[:-forecast_out+1]
df.dropna(inplace=True)
y = np.array(df['label'])

print(len(x), len(y))


