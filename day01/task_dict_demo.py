#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: task_dict_demo.py
@time: 2017/4/28 14:41
将列表中的数字 大于66的存在看k1中 小于66的存在k2中
"""


dic = {}
all_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]

for i in all_list:
    if i >= 66:
        if 'k1' in dic:
            dic['k1'].append(i)
        else:
            dic['k1'] = [i, ]
    else:
        if 'k2' in dic:
            dic['k2'].append(i)
        else:
            dic['k2'] = [i, ]
print dic