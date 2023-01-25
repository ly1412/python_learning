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
### np.clip函数
clip(min, max)
### pyplot.figure figsize参数
(9, 7) width = 9英寸，height=7英寸
### pyplot.savefig
pyplot.savefig("1.png")
### pandas 拼接
append(deprecated, ignore_index=True)
### pandas 重定义index name
rename(index={15: 'Total'})
### pandas reindex
reindex(columns=data.columns, fill_value=0) fill_value空值自动填充，索引是自动的
### pandas apply
data.apply(enum_row, axis=1) axis控制方向 0为横向方向，按列枚举，1为纵向方向按行枚举,以enum_row函数进行逐行处理


