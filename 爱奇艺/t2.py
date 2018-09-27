#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
库特君的面条
题目描述：
库特君在吃面条！
他将面条放在了数轴上，每根面条对应数轴上的两个点a和b，他想知道在任意两根面条不重叠(端点可以重叠）
的情况下最多能选出多少根面条。
1 <= n <= 100
-999 <= a <b <= 999

输入
第一行一个整数N
接下来，N行，每行2个空格分隔的整数a和b(注意：a有可能大于b)

输出
一个数的答案

样例输入
3
6  3
1  3
2  5
样例输出
2
'''


if __name__ == "__main__":
    n = int(input())
    d = []
    for i in range(n):
        (a, b) = (int(i) for i in input().split())
        (a, b) = (a, b) if a < b else (b, a)
        d.append((a, b))
    r = sorted(d, key=lambda x: x[1])
    previous = 0
    result = 0
    for j in range(1, n):
        if r[j][0] >= r[previous][1]:
            result += 1
            previous = j
    print(result+1)
