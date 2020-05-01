import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
import pandas as pd 

accs = []

for i in range(10):

	df = pd.read_csv('breast-cancer.data')
	df.replace('?',-99999, inplace=True)
	df.drop(['id'],1,inplace=True)

	x = np.array(df.drop(['class'],1))
	y = np.array(df['class'])

	xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.5)

	clf = neighbors.KNeighborsClassifier()
	clf.fit(xtrain,ytrain)
	acc = clf.score(xtest,ytest)
#	print(acc)
#	example= np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1]])
#	example= example.reshape(len(example),-1)
#	pred = clf.predict(example)
#	print(pred)
	
	accs.append(acc)
print(sum(accs)/len(accs))

