#!/usr/bin/python
# -*- coding:utf-8 -*-


from scipy.integrate import odeint
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(state, t):
    # print w
    # print t
    sigma = 10
    rho = 28
    beta = 3
    x, y, z = state
    return np.array([sigma*(y-x), x*(rho-z)-y, x*y-beta*z])


if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # fiture1
    s0 = (0., 1., 0.)
    t = np.arange(0, 30, 0.01)
    s = odeint(lorenz, s0, t)
    print(s)
