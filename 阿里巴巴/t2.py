#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
# 输入范例:
# <[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>
# 来几首@{singer}的流行歌曲
# 输出范例:
# 0
import re


def find(s, query):
    pa = re.compile(s)
    if re.match(pattern=pa, string=query):
        print('1')
    else:
        print('0')


if __name__ == '__main__':
    s = input().strip()
    query = input().strip()
    find(s, query)
