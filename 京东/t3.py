#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def find(s, T):
    num = 0
    temp1 = s
    temp2 = T
    for i, char in enumerate(s):
        if temp1[i].isdigit() or temp2[i].isdigit():
            if temp1[i] == temp2[i]:
                continue
            else:
                return 0
        else:
            temp1 = temp1.replace(char, str(num))
            temp2 = temp2.replace(temp2[i], str(num))
            num += 1
    else:
        return 1


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
