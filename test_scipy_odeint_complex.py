import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def diff(y, x, k, n, b):
    res = k * (np.array(x) ** n) + b
    return res


x = np.linspace(0, 10, 100)
y = odeint(func=diff, y0=100.0, t=x, args=(3.0, 2, 4.0))

plt.plot(x, 3.0*(np.array(x) ** 2) + 4.0, label='derivative')
plt.plot(x, y[:, 0], label='origin')
plt.grid()
plt.legend()
plt.show()
