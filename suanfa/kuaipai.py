#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 9:06
# @Author  : wushaohong


def kuaipai(seq):
    i, j = 0, 1
    while True:
        if i >= j:
            return seq


def k2(seq):
    if len(seq) <= 1:
        return seq
    else:
        return k2([value for value in seq[1:] if value < seq[0]]) + seq[0:1] + k2(
            [value for value in seq[1:] if value >= seq[0]])


def k3(seq):
    if len(seq) <= 1:
        return seq
    else:
        small = []
        large = []
        for value in seq[1:]:
            if value >= seq[0]:
                large.append(value)
            else:
                small.append(value)
        return k3(small) + seq[0:1] + k3(large)


if __name__ == '__main__':
    seq = [12, 32, 21, 9, 78, 32, 12, 76, 5]
    seq2 = k3(seq)
    print(seq)
    print(seq2)
