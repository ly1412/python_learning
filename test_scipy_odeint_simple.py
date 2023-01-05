import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def diff(y, x):
    res = np.array(x)
    return res


x = np.linspace(0, 10, 100)
y = odeint(func=diff, y0=0, t=x)

plt.plot(x, np.array(x), label='derivative')
plt.plot(x, y[:, 0], label='origin')
plt.grid()
plt.legend()
plt.show()
