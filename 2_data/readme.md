# pandas
## fuzzywuzzy字符串相似度计算
fuzz.ratio('Python Package', 'PythonPackage')
## group by 数据分组

## pandas.Categorical类型
categorical类似于java enum俩部分 order和字面意思
## roc、auc
### roc曲线：对于分类器模型，x轴：
fpr(误诊率)->FALSE positive rate = false positive/ negative(false positive + true negative)
### y轴：
tpr(真阳性率、灵敏度、recall)->true positive rate = true positive/positive(tp + false negative)
### 特异性：
specificity：1-fpr=tp/negative(false positive + true negative)
### auc值
为roc曲线下的面积值
## label_binarize用法
label_binarize([1, 6], classes=[1, 2, 4, 6])
array([[1, 0, 0, 0],
       [0, 0, 0, 1]])
## zip dic 联用
dict(list(zip(np.arange(n_columns), columns)))
## pandas rename，pandas dataframe定义新列名
data.rename(columns=new_columns, inplace=True)
## pandas.get_dummies return DataFrame
s = pd.Series(['男', '女'])
print(type(pd.get_dummies(s)))
print(pd.get_dummies(s))
## categorical的编码
y = np.array(pd.Categorical(data['accept']).codes)
## train test 分割
from sklearn.model_selection import train_test_split
x, x_test, y, y_test = train_test_split(x, y, test_size=0.3)
## 随机森林模型构造（决策树个数，决策树最大深度）
clf = RandomForestClassifier(n_estimators=50, max_depth=7)
## 精确度计算（真实值，预测值）
metrics.accuracy_score(y_test, y_test_hat)
## pandas ravel()
函数将展平的基础数据作为ndarray返回
## roc曲线计算
fpr, tpr, _ = metrics.roc_curve(y_test_one_hot.ravel(), y_test_one_hot_hat.ravel())
## auc值计算 
### Micro AUC
auc = metrics.auc(fpr, tpr) or  auc = metrics.roc_auc_score(y_test_one_hot, y_test_one_hot_hat, average='micro')
### Macro 
auc = metrics.roc_auc_score(y_test_one_hot, y_test_one_hot_hat, average='macro')
## pyplot的xticks即x轴的刻度设置,如:以月份在x轴显示
plt.xsticks(x, calendar.month_name[1:13], color='blue', rotation=60)
## np.ptp 扁平化后寻找峰值
array = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
array_output1 = np.ptp(array)
返回7