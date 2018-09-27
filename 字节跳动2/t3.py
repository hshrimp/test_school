#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 18:42
# @Author  : wushaohong
'''
题目描述：
/a/././b//../../c/
/c
'''

if __name__ == '__main__':
    path = input()
    s = path.split('/')
    if s[-1] == '':
        m = s[-2]
    else:
        m = s[-1]
    print('/' + m)
