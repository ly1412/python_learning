import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data = 2*np.random.rand(10000, 2)-1
# print(data)
# x = data[:, 0]
# y = data[:, 1]
#
# idx = x**2 + y**2 <= 1
# hole = x**2 + y**2 < 0.25
# idx = np.logical_and(idx, ~hole)
# plt.plot(x[idx], y[idx], 'go', markersize=1)
# plt.show()

# p = np.random.rand(10000)
# np.set_printoptions(edgeitems=5000, suppress=True)
# print(p)
#
# plt.hist(p, bins=20, color='g', edgecolor='k')
# plt.show()
# N = 10000
# times = 100
# z = np.zeros(N)
# for i in range(times):
#     z += np.random.rand(N)
#
# z /= times
#
# plt.hist(z, bins=20, color='g', edgecolor='k')
# plt.show()

# d = np.random.rand(3, 4)
# print(d)
# print(type(d))
#
# data = pd.DataFrame(data=d, columns=list('梅兰竹菊'))
# print('-'*50)
# print(data)
# print(type(data))
#
# print(data[list('竹菊')])
#
# data.to_csv('data.csv', header=True, index=True)

# d = np.random.rand(100)*6-4
# print(d)
#
# plt.plot(d, 'r.')
# plt.show()

x = np.arange(0, 10, 0.1)
y = x**x
plt.plot(x, y, 'r-', linewidth=3)
plt.show()
