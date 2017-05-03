#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 二分查找.py
@time: 2017/5/1 15:00
"""

data = list(range(1, 600, 3))


def binary_search(data_source, find_n):
    mid = len(data_source)//2
    if len(data_source) >= 1:
        if data_source[mid] > find_n:
            print('data in left of [%s]' % data_source[mid])
            binary_search(data_source[:mid], find_n)
        elif data_source[mid] < find_n:
            print('data in right of [%s]' % data_source[mid])
            binary_search(data_source[mid:], find_n)
        else:
            print('found find_s:', data_source[mid])
    else:
        print('cannot find >>>>>')

binary_search(data, 1)


if __name__ == '__main__':
    # print(data[2.5])
    pass