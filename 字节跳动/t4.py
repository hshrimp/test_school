#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong

def find(i, j, maps, n, m):
    queue, count, maps[i][j] = [[i, j]], 1, 0
    while queue:
        x, y = queue[0][0], queue[0][1]
        for i, j in zip([-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]):
            xt, yt = x + i, y + j
            if -1 < xt < n and -1 < yt < m and maps[xt][yt] != 0:
                queue.append([xt, yt])
                maps[xt][yt] = 0
                count += 1
        del queue[0]
    return count


if __name__ == '__main__':
    maps = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
    n, m = 10, 10  # 输入行列
    teams = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0:
                teams.append(find(i, j, maps, n, m))
    print(len(teams), max(teams))
