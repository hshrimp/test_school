#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
题目描述：
给定一个合法的表达式字符串，其中只包含非负整数、加法、减法以及乘法符号（不会有括号），
例如7+3*4*5+2+4-3-1，请写程序计算该表达式的结果并输出

输入
输入有多行，每行是一个表达式，输入以 END 作为结束；

输出
每行表达式的计算结果；

样例输入
7+3*4*5+2+4-3-1
2-3*1
END
样例输出
69
-1
'''


def cheng(temp):
    temp3 = temp.split('*')
    count = 1
    for x in temp3:
        count *= int(x)
    return count


def jian(temp):
    temp2 = temp.split('-')
    count = cheng(temp2[0])
    for x in temp2[1:]:
        count -= cheng(x)
    return count


def find(text):
    count = 0
    add = text.split('+')
    for temp in add:
        count += jian(temp)
    print(count)

if __name__ == '__main__':
    texts = []
    tag = True
    while tag:
        text = input()
        if text != 'END':
            texts.append(text)
        else:
            tag = False
    for text in texts:
        find(text)
