#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
题目描述：
高贵的蕾米莉亚大小姐每天需要饮用定量 B 型血的红茶以保持威严，并且要分两杯在不同时段饮用。
女仆长十六夜咲夜每天可以制作很多杯不同剂量 B 型血的红茶供蕾米莉亚大小姐饮用。
某日，你和天才妖精琪露诺偷偷潜入红魔馆被咲夜抓住，要求在今日份的红茶中挑出所有满足大小姐要求的茶杯，否则……

输入
每个样例有三行输入，第一行输入表示茶杯个数，第二行输入表示每份茶杯里的 B 型血剂量，第三行表示大小姐今天的定量

输出
对每一个样例，输出所有可能的搭配方案，如果有多种方案，请按每个方案的第一杯 B 型血剂量的大小升序排列。
如果无法找到任何一种满足大小姐的方案，输出一个字符 ⑨ 并换行。
样例输入
7
2 4 6 1 3 5 7
7
样例输出
1 6
2 5
3 4
'''


def find(jl, num, n):
    anwser = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if jl[i] + jl[j] == num:
                if jl[i] <= jl[j]:
                    anwser.append([jl[i], jl[j]])
                else:
                    anwser.append([jl[j], jl[i]])
    if len(anwser) == 0:
        print('⑨')
    else:
        anwser = sorted(anwser, key=lambda x: x[0])
        for p, q in anwser:
            print(p, q)


if __name__ == '__main__':
    n = int(input())
    jl = [int(x) for x in input().split()]
    num = int(input())
    find(jl, num, n)
