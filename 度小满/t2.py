#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
题目描述：
n个点连成一条链，从左往右依次从1到n编号。
相邻点之间有边相连，一共有n-1条边。所有的边从1到n-1编号，第i条边连接了点i和i+1。
第i个点有点权ai，定义第i条边的权重为wi：有多少点对x，y满足在第i条边的左侧（x≤i），
y在第i条边的右侧（y>i），且x和y的点权不同。
给出每个点的点权，请求出所有边的边权。

输入
第一行输入一个数n。(2≤n≤100000)
第二行输入n个数，a1,a2,…,an (1≤ai≤109)

输出
输出n-1个数，依次为每条边的权重，不要在行末输出多余的空格。
样例输入
3
1 2 1
样例输出
1 1
'''


def count(param, param1, length):
    sum = length - param1.count(param)
    return sum


def find(n, nums):
    w = []
    for i in range(1, n):
        if i == 1:
            w.append(count(nums[0], nums[i:], n - i))
        else:
            sum = w[i - 2] - count(nums[i - 1], nums[:i - 1], i - 1) + count(nums[i - 1], nums[i:], n - i)
            w.append(sum)
    print(' '.join(str(x) for x in w))


if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split()]
    left = dict()
    right = dict()
    find(n, nums)
