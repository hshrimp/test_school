#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
# 8888/1
def find2(ip):
    count = 0
    for i in range(1, 4):
        if len(ip[:i])>1 and ip[0]==0:
            break
        n1 = int(ip[:i])
        if n1 > 255:
            break
        for j in range(i + 1, i + 4):
            if len(ip[i:j])>1 and ip[i]==0:
                break
            n2 = int(ip[i:j])
            if n2 > 255:
                break
            for k in range(j + 1, j + 4):
                if len(ip[j:k]) > 1 and ip[j] == 0:
                    break
                if len(ip[k:]) > 1 and ip[k] == 0:
                    break
                if len(ip[j:k]) == 0:
                    break
                n3 = int(ip[j:k])
                if n3 > 255:
                    break
                if len(ip[k:]) == 0:
                    break
                n4 = int(ip[k:])
                if n4 > 255:
                    continue
                print(n1, n2, n3, n4)
                count += 1
    print(count)


def find(ip):
    if len(ip) < 4:
        print('0')
    if len(ip) == 4:
        print('1')
    # if len(ip) == 5:
    #     return 4
    if len(ip) > 12:
        print('0')
    if 4 < len(ip) <= 12:
        find2(ip)


if __name__ == '__main__':
    ip = input()
    find(ip)
