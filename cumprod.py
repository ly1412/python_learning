import numpy as np


n = 10
v_x = 0.2
f = np.arange(1, n+1).cumprod()
np.set_printoptions(suppress=True)
b = np.array([v_x]*n).cumprod()
print("f:", f)
print("b:", b)
print(np.sum(b / f) + 1)