import numpy as np


x = np.array([1,5])
y = np.array([1,2,3])

t = np.meshgrid(x, y)
print(t[0])
print(t[1])

