import numpy as np


a = [1, 2, 3]
b = [0, 0.5]

print(np.convolve(a, b, mode='valid'))


n = 10
weight = np.ones(n)
weight /= weight.sum()

c = [4.31, 4.42, 4.4,  4.39, 4.52, 4.54, 4.51, 4.44, 4.66, 4.62]


print(np.average(c))

