#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
局长的食物
题目描述：
局长有N种食物，每种食物有Ai份。
每天局长会吃一份食物，或者买一份食物（即每天只能进行吃或买其中的一种动作），这样过了M天
现在局长想知道M天后第p种食物的份数排名（从大到小，相同算并列，例如3 3 2，则排名为1 1 3）
N,M,P<=100,Ai<=1000

输入
第一行N M P
第二行N个数Ai
接下来M行，每行A i或者B i分别表示买一份食物i，吃一份食物i

输出
一个答案

样例输入
3 4 2
5 3 1
B 1
A 2
A 2
A 3
样例输出
1

3 4 1
5 3 1
B 1
A 2
A 2
A 3
'''


def find(num, action):
    for i in range(len(action)):
        act, n = action[i]
        if act == 'A':
            num[n - 1] += 1
        else:
            num[n - 1] -= 1
    return num


def rank(new_num, P):
    s = sorted(new_num, reverse=True)
    index = s.index(new_num[P - 1])
    while index >= 1:
        if new_num[P - 1] == s[index - 1]:
            index -= 1
        else:
            break
    print(index + 1)


if __name__ == '__main__':
    N, M, P = [int(i) for i in input().split()]
    num = [int(i) for i in input().split()]
    action = []
    for i in range(M):
        act, n = input().split()
        n = int(n)
        action.append([act, n])

    new_num = find(num, action)
    rank(new_num, P)
