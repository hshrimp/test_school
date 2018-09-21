#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 18:42
# @Author  : wushaohong
'''
题目描述：
有一个长度为N的序列 a, a中的每个元素都是属于[1, M]中的整数，且a中包含[1, M]中的所有整数。
如: N = 5, M = 3 的序列 a = [1, 3, 2, 3, 1]。 包含[1, 3]中的所有整数，且每个元素都属于[1, 3]。
当序列a的某个连续子序列同样包含[1, M]中的所有整数时，称此连续子序列为完备连续子序列。
现想要求长度最短的完备连续子序列的长度。

输入
第一行是由空格隔开的两个整数分别表示 N 和 M （1 <= M <= N <= 10^5）。
第二行是由空格隔开的 N 个整数按顺序表示序列 a 中的所有元素。

输出
只包含一个整数，表示完备序列的最短长度。

样例输入
10 4
1 3 2 2 4 1 2 3 4 1
样例输出
4

Hint
样例解释
N = 10, M = 4, 序列 a = [1, 3, 2, 2, 4, 1, 2, 3, 4, 1]
其中第6到第9元素[1, 2, 3, 4]和第7到第10元素[2, 3, 4, 1]都是最短的完备连续子序列，长度均为4。

数据范围
对于 60% 的数据: 1 <= M <= N <= 1000
对于 100% 的数据: 1 <= M <= N <= 10^5
'''


def find(n, m, a):
    length = m
    while length < n:
        i = 0
        temp = set()
        while i < n - length:
            if len(temp) > 0:
                while a[i + length-1] in temp:
                    i += 1

            temp = set(a[i:i + length])
            if len(temp) == m:
                return length
            # if temp == tag:
            #     return length
            # if a[i + length] in temp:
            #     i += 1
            i += 1
        length += 1
    return n


if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    a = input().split()
    # tag = set(str(x) for x in range(1, m + 1))
    num = find(n, m, a)
    print(num)
