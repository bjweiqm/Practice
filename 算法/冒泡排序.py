#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 冒泡排序.py
@time: 2017/5/3 11:53
"""


data = [10, 4, 33, 21, 54, 3, 8, 11, 5, 22, 2, 1, 17, 13, 6]

for index, i in enumerate(data[:-1]):
    if i > data[index+1]:
        # data[index+1], data[index] = i, data[index+1]
        tmp = data[index+1]
        data[index+1] = i
        data[index] = tmp

print(data)