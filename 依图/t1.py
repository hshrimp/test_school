#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
题目描述：
一只蚂蚁在一个三阶魔方表面爬行，魔方悬挂在空中，因此蚂蚁可以到达魔方的任意面。
每一时刻，蚂蚁会进行如下三种动作的一种：左转90度，右转90度，或沿当前方向移动到相邻的格子。
对于一个三阶魔方，我们将其6个面按下图形式展开，并给六个面 0-5 编号（如图中深色数字所示），
并给每个面上的格子 0-8 编号（如图中白色数字所示）：

蚂蚁初始位于0号面的4号格子，朝向5号格子。‍现给出魔方上每个格子的颜色，以及蚂蚁各时刻的动作，
要求给出蚂蚁各时刻所在格子的颜色。

正在上传...
输入
第1-6行：依次给出魔方上编号0-5的面的颜色，每行一个长度为9的字符串，字符串由小写字母构成，
每个字母代表一种颜色，9个字符依次表示该面上编号0-8的格子上的颜色。
第7行：一个长度为N的有字母"L"，"R"，或"M"构成的字符串，表示蚂蚁各个时刻的动作。
其中"L"表示左转90度，"R"表示右转90度，"M"表示移动至相邻格子，1<=N<=10000。

输出
第一行：一个长度为N的字符串，表示蚂蚁各时刻所在格子的颜色。


样例输入
abcdefghi
ooooooooo
ppppppppp
qqqqqqqqq
rrrrrrrrr
sssssssss
LMMMMMMMMMMMMRRRMMMMMMMMMMMM
样例输出
ebrrrpppsssheeeedqqqpppooofe
'''


def removal(word, tag, word_len):
    return 3 * (tag_len - word_len)


def insertion(word, tag, word_len):
    return 3 * (word_len - tag_len)


def substitution(word, tag):
    score = 0
    for i in range(tag_len):
        if tag[i] != word[i]:
            if tag[i] in li1:
                if word[i] in li1:
                    score += 1
                else:
                    score += 2
            else:
                if word[i] in li2:
                    score += 1
                else:
                    score += 2
    return score


def compute(word, tag):
    word_len = len(word)
    # tag_len=len(tag)
    score = 0
    if tag_len > word_len:
        score += removal(word, tag, word_len)
    elif tag_len < word_len:
        score += insertion(word, tag, word_len)
    else:
        score += substitution(word, tag)
    return [word, score]


if __name__ == '__main__':
    k = input().split()
    tag = k[0].lower()
    dic_list = k[1:]
    #
    li1 = 'q w e r t a s d f g z x c v '
    li2 = 'y u i o p h j k l b n m'
    scores = []
    tag_len = len(tag)
    for word in dic_list:
        word = word.lower()
        scores.append(compute(word, tag))
    scores = sorted(scores, key=lambda x: x[1])
    if len(scores) >= 3:
        print(scores[0][0], scores[1][0], scores[2][0])
    else:
        for word in scores:
            print(word[0], end=' ')
