#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong


'''
输入一个字符串，打印这个字符串中字符的全排列。
eg：
输入：abc
输出：abc acb bac bca cab cba
思路:将求字符串的全排列分解为两步：
第一步是确定第一个位置的字符，就是第一个位置与后边的所有字符进行交换。
第二步，就是对除了第一个位置的后边所有位置的字符进行相同处理；直至剩下一个字符，打印；
'''

def perm(s=''):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in perm(s[0:i] + s[i + 1:]):
            sl.append(s[i] + j)
    return sl


def main():
    # 可能包含重复的串
    perm_nums = perm('abb')
    # 对结果去重
    no_repeat_nums = list(set(perm_nums))
    print('perm_nums', len(perm_nums), perm_nums)
    print('no_repeat_nums', len(no_repeat_nums), no_repeat_nums)
    pass


if __name__ == '__main__':
    main()
