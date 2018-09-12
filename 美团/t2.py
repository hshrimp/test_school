#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 18:42
# @Author  : wushaohong
# 10 2
# 1 0 0 1 0 1 0 1 0 1
# 5
def find(indexs, k, length):
    max_num = 0
    for i in range(len(indexs) - k + 1):
        if i == 0:
            max_num = indexs[k]
        elif i == len(indexs) - k:
            num = length - indexs[i - 1] - 1
            if num > max_num:
                max_num = num
        else:
            num = indexs[i + k] - indexs[i - 1] - 1
            if num > max_num:
                max_num = num
    print(max_num)



if __name__ == '__main__':
    length, k = input().split()
    seq = input().split()
    k = int(k)
    length=int(length)
    seq = [int(n) for n in seq]
    indexs = [x for x in range(len(seq)) if seq[x] == 0]
    find(indexs, k, length)
