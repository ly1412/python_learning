# -*- coding:utf-8 -*-

import pandas as pd


s = pd.Series(['男', '女'])
print(type(pd.get_dummies(s)))
print(pd.get_dummies(s))
