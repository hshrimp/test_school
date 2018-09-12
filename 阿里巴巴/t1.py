#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 18:42
# @Author  : wushaohong
# 输入范例:
# singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
# 请播放周杰伦的七里香给我听
# 输出范例:
# 请播放 周杰伦/actor,singer 的 七里香/song 给我听
def extract(s):
    temp = s.strip().split(';')
    d = dict()
    length = []
    for item in temp:
        key, values = item.split('_')
        values = values.split('|')
        for i in values:
            if len(length) == 0:
                length.append(i)
            else:
                for j in range(len(length)):
                    if len(i) > len(length[j]):
                        length.insert(j, i)
                else:
                    length.append(i)
        d[key] = values
    return d, length


def find(d, length, inp):
    string = []
    for item in length:
        if item in inp:
            i, j = inp.split(item)
            for k, v in d.items():
                if item in v:
                    string.append(k)
            return find(d, length, i) + ' ' + item + '/' + ','.join(string) + ' ' + find(d, length, j)
    else:
        return inp


if __name__ == '__main__':
    s = input()
    my_dict, length = extract(s)
    inp = input().strip()
    string = find(my_dict, length, inp)
    print(string)
