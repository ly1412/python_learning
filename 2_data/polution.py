#!/usr/bin/python
# -*- encoding: utf-8
import matplotlib as mpl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor


if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = ['simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    data = pd.read_csv('data_file/C0911.csv', header=0)
    x = data['H2O'].values
    print(x)

    # error detection
    width = 500
    delta = 10
    eps = 0.15
    N = len(x)
    p = []
    abnormal = []
    for i in np.arange(0, N - width, delta):
        s = x[i:i+width]
        p.append(np.ptp(s))
        if np.ptp(s) > eps:
            abnormal.append(list(range(i, i+width)))
    abnormal = np.unique(abnormal)
    plt.figure(facecolor='w')
    plt.plot(p, lw=1)
    plt.grid(visible=True, ls=':', color='#404040')
    plt.title('固定间隔$H_2O$含量的差值', fontsize=16)
    plt.xlabel('时间', fontsize=15)
    plt.xlabel('差值', fontsize=15)
    plt.show()

    plt.figure(figsize=(11, 5), facecolor='w')
    plt.subplot(131)
    plt.plot(x, 'r-', lw=1, label='原始数据')
    plt.title('实际排放数据', fontsize=16)
    plt.legend(loc='upper right')
    plt.grid(visible=True, ls=':', color='#404040')

    plt.subplot(132)
    t = np.arange(N)
    plt.plot(t, x, 'r-', lw=1, label='原始数据')
    plt.plot(abnormal, x[abnormal], 'go', markeredgecolor='g', ms=2, label='异常值')
    plt.legend(loc='upper right')
    plt.title('异常检测', fontsize=16)
    plt.grid(visible=True, ls=':', color='#404040')

    # 异常校正(预测)
    plt.subplot(133)
    select = np.ones(N, dtype=bool)
    select[abnormal] = False
    t = np.arange(N)
    dtr = DecisionTreeRegressor(criterion='squared_error', max_depth=10)
    br = BaggingRegressor(dtr, n_estimators=10, max_samples=0.3)
    br.fit(t[select].reshape(-1, 1), x[select])
    y = br.predict(np.arange(N).reshape(-1, 1))
    y[select] = x[select]
    plt.plot(x, 'g--', lw=1, label='原始值')    # 原始值
    plt.plot(y, 'r-', lw=1, label='校正值')     # 校正值
    plt.legend(loc='upper right')
    plt.title('异常值校正', fontsize=16)
    plt.grid(visible=True, ls=':', color='#404040')

    plt.tight_layout()
    plt.suptitle('排污数据的异常值检测与校正', fontsize=18)
    plt.show()