#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
世界杯开幕式

世界杯开幕式会在球场C举行，球场C的球迷看台可以容纳M*N个球迷。在球场售票完成后，现官方想统计此次开幕式一共有多少个球队球迷群体，最大的球队球迷群体有多少人。
同球队的球迷群体会选择相邻座位，不同球队的球迷群体会选择不相邻的座位。（注解：相邻包括前后相邻、左右相邻、斜对角相邻。）

给定一个M*N的二维球场，0代表该位置没人坐，1代表该位置有球迷，希望输出球队群体的个数P， 最大的球队群体人数Q。
'''
def getSum(i, j, n, m, maps):  # [i, j]单阵入口，[n,m]矩阵维度数，maps矩阵
    queue, sump, maps[i][j] = [[i, j]], 1, 0  # 初始化队列
    while queue:
        x, y = queue[0][0], queue[0][1]  # 获取队列头元素
        for dx, dy in zip((-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)):  # 8个方向
            nx, ny = x + dx, y + dy
            if -1 < nx < n and -1 < ny < m and maps[nx][ny] != 0:
                queue.append([nx, ny])  # 入队
                sump += maps[nx][ny]  # 累计球队人数
                maps[nx][ny] = 0  # 累计过的位置设置为0
        del queue[0]  # 出队
    return sump  # 返回其中一个球队的人数总和


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

    team = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0: team.append(getSum(i, j, n, m, maps))  # 获取每个球队和
    print(str(len(team)) + ',' + str(max(team)))
