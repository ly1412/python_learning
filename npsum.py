import numpy as np


a = np.array([[0, 2, 1], [3, 5, 6], [0, 1, 1]])
print(a)
b = np.sum(a, desity=True)  # 一列相加，不保持二维特性
c = np.sum(a, axis=0, keepdims=True) # 一列相加，保持二维特性
print(b)
print(c)