#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 二位数组旋转.py
@time: 2017/5/1 15:37
"""


data = [[col for col in range(4)] for raw in range(4)]      # 创建一个二维数组
for n in data:
    print(n)

print('\n')

for i in range(len(data)):                                # 外层循环
    for j in range(i+1, len(data)):                       # 内层循环
        # 交换数据
        temp = data[i][j]
        data[i][j] = data[j][i]
        data[j][i] = temp

for n in data:
    print(n)