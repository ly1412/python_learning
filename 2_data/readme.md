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
## pandas.get_dummies
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
