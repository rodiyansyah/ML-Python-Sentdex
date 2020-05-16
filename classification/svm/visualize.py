from mpl_toolkits.mplot3d import  axes3d
import matplotlib.pyplot as plt
from matplotlib import  style
import numpy as np
import math
style.use('ggplot')

def simple_transformation(x1,x2):
    return x1**2, 2*x2**2, x2

c1 = np.array([[1,1],
              [3,1],
              [2,1],
              [2,0],
              [3,6],
              [3,4],
              [-5,4]])

c2 = np.array([[2,5],
               [1.5,4]])

c13d = np.array([simple_transformation(x[0],x[1]) for x in c1])
c23d = np.array([simple_transformation(x[0],x[1]) for x in c2])

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='3d')

ax1.scatter(c1[:,0], c1[:,1], color='r', marker='*', s=150)
ax1.scatter(c2[:,0], c2[:,1], color='b', marker='^', s=150)

ax2.scatter(c13d[:,0], c13d[:,1], c13d[:,2], c='r', marker='*', s=150)
ax2.scatter(c23d[:,0], c23d[:,1], c23d[:,2], c='b', marker='^', s=150)

plt.show()







