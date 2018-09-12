#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************
def fd(string):
    li = '0'
    count = 1
    for i in range(1, len(string)):
        for j in range(i):
            if string[j] == string[i]:
                li += li[j]
            else:
                li += str(count)
                count += 1
    return li


def find(s, T):
    d1 = fd(s)
    d2 = fd(T)
    if d1 == d2:
        return 1
    else:
        return 0


def solve(S, T):
    count = 0
    length = len(T)
    for i in range(len(S) - length + 1):
        s = S[i:i + length]
        num = find(s, T)
        count += num
    return count


# ******************************结束写代码******************************


try:
    _S = input()
except:
    _S = None

try:
    _T = input()
except:
    _T = None

res = solve(_S, _T)

print(str(res) + "\n")
