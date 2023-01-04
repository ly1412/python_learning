#!/usr/bin/python
#  -*- coding:utf-8 -*-

import cv2

image = cv2.imread('../lena.png')
print(image)
print(type(image))
print(image.shape)