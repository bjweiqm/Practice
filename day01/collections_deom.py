#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: collections_deom.py
@time: 2017/4/28 18:13
"""

"""
import collections
# 可命名元组
# 创建类
MytupleClass = collections.namedtuple('MyTupleClass', ['x', 'y', 'z'])
obj = MytupleClass(11, 22, 33)  # x = 11 x = 22  z = 33
print(obj.x)
print(obj.y)
print(obj.z)
print(dir(obj))
"""

"""
import collections
# 有序字典
dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
dic['k3'] = 'v4'
"""

"""
对字典的补充：
import collections
1. Counter()    # 实现计数器  Counter({'a': 6, 'j': 5, 'f': 4, 'l': 3, 'g': 2, 'o': 2, 'e': 1, 'd': 1, 'i': 1})


import collections
obj = collections.Counter('fajfjaeoifjoaglalgajdajfl')
# print (obj)
ret = obj.most_common(4)            # 从多到少 拿到前4位
# print( ret)
"""