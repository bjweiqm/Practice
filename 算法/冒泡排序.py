#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 冒泡排序.py
@time: 2017/5/3 11:53
"""


data = [10, 4, 33, 21, 54, 3, 8, 11, 5, 22, 2, 1, 17, 13, 6]

for j in range(1, len(data)):
    for i in range(len(data)-j):
        if data[i] > data[i+1]:
            tmp = data[i+1]   # 把4 保存
            data[i+1] = data[i]  # 把10 =》4
            data[i] = tmp   # 把 4 +> 10

print(data)