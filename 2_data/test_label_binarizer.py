# -*- coding:utf-8 -*-

from sklearn.preprocessing import label_binarize


print(label_binarize([1, 6], classes=[1, 2, 4, 6]))