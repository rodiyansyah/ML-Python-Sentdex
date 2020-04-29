import numpy as np
from math import sqrt
import warnings
from collections import Counter
import pandas as pd 
import random


def k_NN(data, predict, k=3):
	if len(data) >= k:
		warnings.warn('K is set to a value less than total data')
	dis = []
	for group in data:
		for fatures in data[group]:
			ed = np.linalg.norm(np.array(fatures)-np.array(predict))
			dis.append([ed, group])

	votes = [i[1] for i in sorted(dis)[:k]]
	print(Counter(votes).most_common(1 ))
	vote = Counter(votes).most_common(1)[0][0]
	return vote


df = pd.read_csv('breast-cancer.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'],1, inplace=True)
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

test_size =0.2
trainSet = {2:[], 4:[]}
testSet = {2:[], 4:[]}
trainData = full_data[:-int(test_size*len(full_data))]
testData = full_data[-int(test_size*len(full_data)):]


for i in trainData: 
	trainSet[i[-1]].append(i[:-1])


for i in testData: 
	testSet[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in testSet:
	for data in testSet[group]:
		vote =k_NN(trainSet, data, k=5)
		if group == vote:
			correct +=1
		total +=1

print(total)

print('accuracy: ', correct/total)


