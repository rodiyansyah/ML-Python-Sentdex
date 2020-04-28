import numpy as np
import math

x = [1,2,3,4,5,6,7,8,9,10]

fo = int(math.ceil(0.2*len(x)))


x_late = x[-fo:]

x = x[:-fo]


print(x_late)

print(x)