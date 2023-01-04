#!/usr/bin/python
#  -*- coding:utf-8 -*-

import numpy as np
import math
N = 20


def calc_e(n):
    sum_value = 1.0
    for nn in range(1, n):
        sum_value += 1.0 / math.factorial(nn)
    return sum_value


if __name__ == "__main__":
    print(calc_e(N))