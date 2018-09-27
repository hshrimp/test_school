#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
题目描述：
给定三种类型的小球P、Q、R，每种小球的数量分别为np、nq、nr个。
现在想将这些小球排成一条直线，但是不允许相同类型的小球相邻，问有多少种排列方法。
如若np=2，nq=1，nr=1则共有6种排列方式：PQRP，QPRP，PRQP，RPQP，PRPQ以及PQPR。
 如果无法组合出合适的结果，则输出0。

输入
一行以空格相隔的三个数，分别表示为np，nq，nr。

输出
排列方法的数量。

15 15 15
2786716100592
'''


def find(p, q, r, tag):
    if p > q + r + 1 or q > p + r + 1 or r > p + q + 1:
        return 0
    elif p < 0 or q < 0 or r < 0:
        return 0
    elif p + q + r == 1:
        if (tag == 'p' and p == 1) or (tag == 'q' and q == 1) or (tag == 'r' and r == 1):
            return 0
        else:
            return 1
    elif p + q + r == 2:
        if (p == 2) or (q == 2) or (r == 2):
            return 0
        elif (tag == 'p' and p == 1) or (tag == 'q' and q == 1) or (tag == 'r' and r == 1):
            return 1
        else:
            return 2
    else:
        if tag == ' ':
            a = find(p - 1, q, r, 'p')
            b = find(p, q - 1, r, 'q')
            c = find(p, q, r - 1, 'r')
            return a + b + c
        if tag == 'p':
            if str([p, q - 1, r, 'q']) not in li.keys():
                li[str([p, q - 1, r, 'q'])] = find(p, q - 1, r, 'q')
            if str([p, q, r - 1, 'r']) not in li.keys():
                li[str([p, q, r - 1, 'r'])] = find(p, q, r - 1, 'r')
            return li[str([p, q - 1, r, 'q'])] + li[str([p, q, r - 1, 'r'])]
        if tag == 'q':
            if str([p - 1, q, r, 'p']) not in li.keys():
                li[str([p - 1, q, r, 'p'])] = find(p - 1, q, r, 'p')
            if str([p, q, r - 1, 'r']) not in li.keys():
                li[str([p, q, r - 1, 'r'])] = find(p, q, r - 1, 'r')
            return li[str([p - 1, q, r, 'p'])] + li[str([p, q, r - 1, 'r'])]
        if tag == 'r':
            if str([p, q - 1, r, 'q']) not in li.keys():
                li[str([p, q - 1, r, 'q'])] = find(p, q - 1, r, 'q')
            if str([p - 1, q, r, 'p']) not in li.keys():
                li[str([p - 1, q, r, 'p'])] = find(p - 1, q, r, 'p')
            return li[str([p, q - 1, r, 'q'])] + li[str([p - 1, q, r, 'p'])]


if __name__ == '__main__':
    p, q, r = [int(x) for x in input().split()]
    li = dict()
    num = find(p, q, r, ' ')
    print(num)
