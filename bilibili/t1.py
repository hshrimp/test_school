#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wushaohong
'''
题目描述：
小A参加了一个n人的活动，每个人都有一个唯一编号i(i>=0 & i<n)，其中m对相互认识，
在活动中两个人可以通过互相都认识的一个人介绍认识。现在问活动结束后，小A最多会认识多少人？

输入
第一行聚会的人数：n（n>=3 & n<10000）； 第二行小A的编号: ai （ai >= 0 & ai < n)；
 第三互相认识的数目: m （m>=1 & m < n(n-1)/2）； 第4到m+3行为互相认识的对，以','分割的编号。

输出
输出小A最多会新认识的多少人？

样例输入
7
5
6
1,0
3,1
4,1
5,3
6,1
6,5
样例输出
3
'''


def find2(a, temp):
    all = set()
    for nums in temp:
        if a in nums:
            all.add(nums[0])
            all.add(nums[1])
            know.remove(nums)
    return all


def find(n, a, know, num):
    temp = list(know)
    all = find2(a, temp)
    ar_know = len(all)
    count = 0
    while know or count != 0:
        temp = list(know)
        count = 0
        for nums in temp:
            if nums[0] in all or nums[1] in all:
                count += 1
                all.add(nums[0])
                all.add(nums[1])
                know.remove(nums)
    print(len(all) - ar_know)


if __name__ == '__main__':
    n = int(input())
    a = int(input())
    num = int(input())
    know = []
    for i in range(num):
        num1, num2 = [int(x) for x in input().split(',')]
        know.append([num1, num2])
    find(n, a, know, num)
