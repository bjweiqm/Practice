#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 递归.py
@time: 2017/5/1 14:14

# 直接或间接地调用自身算法的过程
1. 递归就是在函数里调用自身
2. 必须有一个明确的递归结束条件。
3. 解题的运算效率较低，不提倡使用递归算法设计程序
4. 递归过多会造成内存溢出，
"""

# 裴波那契数列: 第三个值为前两个数的和


def func(arg1, arg2, stop):
    if arg1 == 0:
        print(arg1, arg2)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3 < stop:
        func(arg2, arg3, stop)

func(0, 1, 30)