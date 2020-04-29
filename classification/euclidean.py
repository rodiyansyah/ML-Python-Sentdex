import numpy as np
from math import sqrt
import matplotlib.pyplot as plt 
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')



dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_feature=[5,7]

#[[plt.scatter(ii[0], ii[1], color=i) for ii in dataset[i]] for i in dataset]
#plt.scatter(new_feature[0],new_feature[1])
#plt.show()

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

res = k_NN(dataset, new_feature, k=3)
print(res)

[[plt.scatter(ii[0], ii[1], color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_feature[0],new_feature[1], color=res)
plt.show()