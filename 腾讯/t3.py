#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 18:42
# @Author  : wushaohong
'''
7 14
2
'''


def find(x, n):
    count = 1
    i = n
    while x > i:
        x -= i
        i -= 1
        count += 1
    print(count)


if __name__ == '__main__':
    x, y = [int(x) for x in input().split()]
    num = x + y
    count, i = 0, 1
    while count != num:
        count += i
        i += 1
    find(x, i-1)
