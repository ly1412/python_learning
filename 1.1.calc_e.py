#!/usr/bin/python
#  -*- coding:utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt


def calc_e_small(v_x):
    n = 20
    f = np.arange(1, n+1).cumprod()
    b = np.array([v_x]*n).cumprod()
    return np.sum(b / f) + 1


def calc_e(_x):
    reverse = False
    if _x < 0:
        reverse = True
        _x = -_x
    ln2 = 0.69314718055994530941723212145818
    c = _x / ln2
    a = int(c + 0.5)
    b = _x - a*ln2
    v_y = (2 ** a) * calc_e_small(b)
    if reverse:
        return 1/v_y
    return v_y


if __name__ == "__main__":
    t1 = np.linspace(-2, 0, 10, endpoint=False)
    t2 = np.linspace(0, 4, 20)
    t = np.concatenate((t1, t2))
    print(t)
    y = np.empty_like(t)
    for i, x in enumerate(t):
        y[i] = calc_e(x)
        print('e^', x, ' = ', y[i], '(近似值)\t', math.exp(x), '(真实值)')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    plt.figure(facecolor='w')
    plt.plot(t, y, 'r-', t, y, 'go', linewidth=2, markeredgecolor='k')
    plt.title('Taylor展式的应用 - 指数函数', fontsize=18)
    plt.xlabel('X', fontsize=15)
    plt.ylabel('exp(X)', fontsize=15)
    plt.grid(True, ls=':')
    plt.show()