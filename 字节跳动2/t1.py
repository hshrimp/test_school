#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
题目描述：
輸入：
5
bytedance
toutiaohao
toutiaoapp
iesaweme
iestiktok

輸出：
b
toutiaoh
toutiaoa
iesa
iest

'''


def find(words):
    last = [x for x in range(len(words))]
    temp = list(words)
    for i in range(1000000):
        li = []
        for index, word in zip(last, temp):
            if len(word) > i:
                li.append(word[:i])
            else:
                temp.remove(word)
                last.remove(index)
                if len(last) <= 1:
                    return words
        for j, value in zip(list(last), li):
            if li.count(value) == 1:
                words[j] = words[j][:i]
                index = last.index(j)
                last.remove(j)
                temp.remove(temp[index])
                if len(last) == 1:
                    words[last[0]] = words[last[0]][:i]
                    return words


if __name__ == '__main__':
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        words.append(list(word))
    find(words)
    for li in words:
        print(''.join(li))
