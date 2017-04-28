#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: set_demo.py
@time: 2017/4/28 17:19
"""
for i in dir(set()):

    if not str(i).startswith('_'):
        print i


s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

s1.intersection(s2)                 # s1 & s2
print(s1 & s2)                      # 交集 （在是s1和s2中都存在 ）
s1.union(s2)                        # s1 | s2
print(s1 | s2)                      # 合集 （两个集合中都存在的数据 上当与s1+s2）
s1.symmetric_difference(s2)         # s1 ^ s2
print(s1 ^ s2)                      # 对称差集 （在s1 或者s2中）
s1.difference(s2)                   # s1 - s2
print(s1 - s2)                      # 差集 （在s1中但不在s2中[s2-s1] 在s2中但不在s1中）

len(s1)                             # set() 的长度

'x' in s2                           # 测试'x'是否是s2的成员
'x' not in s2                       # 测试'x'是否不是s2的成员
s1.issubset(s2)                     # 测试是否 s1中的每一项都在s2中
s1.issuperset(s2)                   # 测试是否 s2中的每一项都在s1中

s1.add()                            # 添加元素
s1.update(s2)                       # 返回增加了set ’s2‘中元素后的 set ’s1‘  同 s1.update(s2)
s1.difference_update(s2)            # 返回只保留含有set s2 中元素的 set s1
s1.discard(2)                       # 如果 set s1 中存在元素 2 ，则删除

s1.copy()                           # 拷贝元素(浅复制)
s1.pop()                            # 随机删除元素，并返回元素
s1.remove(1)                        # 删除指定的元素 return None

