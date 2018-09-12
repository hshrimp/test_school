#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 11:04
# @Author  : wushaohong
import numpy as np


def find(seq, n):
    lo, hi = 0, len(seq) - 1
    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if seq[mid] > n:
            hi = mid - 1
        elif seq[mid] < n:
            lo = mid + 1
        else:
            return print(mid)
    return print('no in ')


if __name__ == '__main__':
    seq = np.arange(0, 100,2)
    n = 4
    find(seq, n)
