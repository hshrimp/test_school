#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
题目描述：
魔法师小九有n个从左到右依次排成一行的魔法石，第i个魔法石的大小为Ai，Ai在[1, 10^9]的范围内。
同时使用排成一行的n个魔法石可以爆发出很大的威力，但是自己也会受到伤害，
自损伤害数值为魔法石大小的逆序对个数，逆序对是指满足i<j且Ai>Aj的 (i,j) 的对数
（逆序对严格按照定义，如211，则逆序对为2个）。魔法师小九希望减小伤害，
他会选择且仅选择一块魔法石将其大小变成0，请问他最多可以将自损伤害数值降低到多少。

输入
第一行一个数n，表示魔法石的数量。（1≤n≤100000）
接下来一行n个数，第i个数表示Ai。（1≤Ai≤10^9）
输出
两个整数，用一个空格隔开，分别表示最小自损伤害数值和选择的魔法石序号，如果有多种最优选择方案，
输出最小的魔法师序号（序号从1开始）。

样例输入
5
2 5 4 3 1
样例输出
5 2

Hint
样例解释
原逆序对数为7，将第二个魔法石变为0后，2 0 4 3 1共有5个逆序对。
'''


def find(n, nums):
    reverse_num = 0
    max_num = 0
    max_i = 0
    for i in range(n - 1):
        temp = 0
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                reverse_num += 1
                temp += 1
        temp2 = 0
        for k in range(i):
            if nums[k] < nums[i]:
                temp2 += 1
        num = temp - temp2
        if num > max_num:
            max_num = num
            max_i = i + 1
        # cha.append(temp - temp2)
        # print(temp2, temp, temp - temp2)
    # num = max(cha)
    print(reverse_num - max_num, max_i)


if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split()]
    cha = []
    find(n, nums)
