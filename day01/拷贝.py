#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 拷贝.py
@time: 2017/4/30 9:58
深拷贝 浅拷贝
"""

import copy

# 浅拷贝
# copy.copy()
# 深拷贝
# copy.deepcopy()


# 数字 字符串 python内部内置了字符串数字池。无论深浅拷贝 都是拷贝的同样的id地址

# 元组、列表、字典
# 浅拷贝只能拷贝一层。
dic = {
    'k1': 'zhagnsan',
    'k2': 'k3',
    'k4': ['zhao', 'qian', 'sun']
}

dic2 = copy.copy(dic)
print id(dic), id(dic['k4'])
print id(dic2), id(dic2['k4'])
# 修改 dic2 的k4 元素 dic中的k4元素也会变化
dic2['k4'].append('li')
print dic

dic1 = copy.deepcopy(dic)
dic1['k4'].append('zhou')
# 深拷贝后 修改 dic1中的k4元素， dic中的k4元素不会变化
print dic, id(dic)
print dic1, id(dic1)