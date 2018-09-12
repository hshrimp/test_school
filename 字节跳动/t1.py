#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
# abc3
def find(string):
    max_len = 0
    for i in range(len(string)):
        temp = [string[i]]
        for j in range(i + 1, len(string)):
            if string[j] in temp:
                if len(temp) > max_len:
                    max_len = len(temp)
                break
            else:
                temp.append(string[j])
            if j == len(string) - 1:
                if len(temp) > max_len:
                    max_len = len(temp)


    print(max_len)


if __name__ == '__main__':
    s = input()
    find(s)
