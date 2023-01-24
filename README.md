# python_learning
## python math
### 自然对数e近似计算
### π值计算
### 随机森林正确率计算
### 阶乘首位数字计算
令 N！=x.yyzz*10^k;
两边对10求对数 —> log10(N!)=log10(x.yyzz)+k;
x.yyzz=10^(log10(N!)-(int)log10(N!))
log10(N!)=log10(1)+log10(2)+...log10(N);
### 乒乓球比赛模拟

## python data
### 判断是否素数算法
只需要计算range(2, math.sqrt(x) + 1)中的所有素数是否被整除，不必判断合数
### filter用法
filter(isFunction, list())
### np tile用法
np.tile(5, n).astype(np.float)  初始化n个初始值为5的array，类型为np.float
### pyplot scatter 参数用法
s: 点大小，c：颜色k=black
