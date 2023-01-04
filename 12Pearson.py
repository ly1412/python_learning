import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def calc_pearson(x, y):
    std1 = np.std(x)
    std2 = np.std(y)
    cov = np.cov(x, y, bias=True)
    print('cov:')
    print(cov)
    print(cov[0, 1])
    return cov[0, 1] / (std1 * std2)


def intro():
    N = 10
    x = np.random.rand(N)
    y = 2 * x + np.random.randn(N) * 0.1
    print(x)
    print(y)
    print('系统计算：', stats.pearsonr(x, y)[0])
    print('手动计算：', calc_pearson(x, y))

def rotate(x, y, theta=45):
    data = np.vstack((x, y))
    # print data
    mu = np.mean(data, axis=1)
    mu = mu.reshape((-1, 1))
    # print mu
    data -= mu
    # print data
    theta *= (np.pi / 180)
    c = np.cos(theta)
    s = np.sin(theta)
    m = np.array(((c, -s), (s, c)))
    return m.dot(data) + mu


def pearson(x, y, tip):
    clrs = list('rgbmycrgbmycrgbmycrgbmyc')
    plt.figure(figsize=(10, 8), facecolor='w')
    for i, theta in enumerate(np.linspace(0, 90, 10)):
        xr, yr = rotate(x, y, theta)
        p = stats.pearsonr(xr, yr)[0]
        print('旋转角度：', theta, 'Pearson相关系数：', p)
        str = '相关系数：%.3f' % p
        plt.scatter(xr, yr, s=40, alpha=0.9, linewidths=0.5, c=clrs[i], marker='o', label=str, edgecolors='k')
    plt.legend(loc='upper left', shadow=True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Pearson相关系数与数据分布：%s' % tip, fontsize=18)
    plt.grid(b=True, ls=':', color='#404040')
    plt.show()

if __name__ == '__main__':
    np.random.seed(0)
    intro()

    N = 1000
    tip = u'二次函数关系'
    x = np.linspace(-1, 1, 101)
    y = x ** 2
    pearson(x, y, tip)