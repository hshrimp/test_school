#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 18:42
# @Author  : wushaohong
'''
2 3 3
9
'''




if __name__ == '__main__':
    x, y, z = [int(x) for x in input().split()]
    count = 0
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            for k in range(1, z + 1):
                if abs(i - j) < k < i + j:
                    count += 1
    print(count % 1000000007)
