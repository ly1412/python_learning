#!/usr/bin/python
# -*- coding:utf-8 -*-


import operator
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb


print('comb(10, 2) = ', comb(10, 2, exact=True))


def bagging(class_count, rate):
    s = 0
    for _i in range(class_count // 2 + 1, n + 1):
        s += comb(class_count, _i) * rate ** _i * (1-rate) ** (class_count - _i)
    return s


if __name__ == "__main__":
    n = 100
    x = np.arange(1, n, 2)
    y = np.empty_like(x, dtype=np.float64)
    for i, t in enumerate(x):
        y[i] = bagging(t, 0.6)
        if t % 10 == 9:
            print(t, '个分类器正确率：', y[i])

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    plt.figure(facecolor='w')
    plt.plot(x, y, 'ro-', lw=2, mec='k')
    plt.xlim(0, n)
    plt.ylim(0.6, 1)
    plt.xlabel('分类器个数', fontsize=16)
    plt.ylabel('正确率', fontsize=16)
    plt.title('随机森林正确率', fontsize=20)
    plt.grid(visible=True, ls=":", color='#606060')
    plt.show()
