#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
2
abab
ababab

5
'''


def find(s, k):
    set_temp = []
    for i in range(len(s) - k + 1):
        if s[i:i + k] not in set_temp:
            set_temp.append(s[i:i + k])
    return set_temp


def find2(b, k, li):
    count = 0
    for i in range(len(b) - k + 1):
        if b[i:i + k] in li:
            count += 1
    print(count)


if __name__ == '__main__':
    k = int(input())
    a = input()
    b = input()
    li1 = find(a, k)
    find2(b, k, li1)
