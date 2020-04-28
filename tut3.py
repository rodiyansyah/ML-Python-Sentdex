from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

#xs =np.array([1,2,3,4,5,6], dtype=np.float64)
#ys =np.array([5,4,6,5,6,7], dtype=np.float64)


def create_dataset(hm, variance, step=2, correlation=False):
	val=1
	ys = []
	for i in range(hm):
		y = val+random.randrange(-variance, variance)
		ys.append(y)

		if correlation and correlation == 'pos':
			val+=step
		elif correlation and correlation == 'neg':
			val -= step

		xs = [i for i in range(len(ys))]

	return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)


def best_fit_slope(xs,ys):
	m= ( ((mean(xs) * mean(ys)) - mean(xs*ys)) /
	   ((mean(xs)*mean(xs)) - mean(xs*xs)) )

	b = mean(ys) - m*mean(xs)
	return m, b

def square_error(ys_orig, ys_line):
	return sum((ys_line-ys_orig)**2) 

def coef_of_determination(ys_orig, ys_line):
	y_mean_line = [mean(ys_orig) for y in ys_orig]
	sqrt_error_regr =square_error (ys_orig, ys_line)
	sqrt_error_y_mean =square_error (ys_orig, y_mean_line)
	return 1 - (sqrt_error_regr/sqrt_error_y_mean)

xs, ys = create_dataset(400, 50, 2, correlation='pos')

m,b = best_fit_slope(xs,ys)
regression_line =[(m*x)+b for x in xs]

predic_x =8
predic_y =(m*predic_x)+b

r_sq = coef_of_determination(ys, regression_line)
print(r_sq)

plt.scatter(xs,ys)
plt.scatter(predic_x,predic_y,color='g')
plt.plot(xs, regression_line, color='r')
plt.show()
