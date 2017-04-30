#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 队列.py
@time: 2017/4/30 9:37
"""


from collections import deque       # 双向队列

# d = deque(maxlen = 30)            # 指定元素最大个数
d = deque()
d.append(1)                         # 添加元素
d.appendleft(3)                     # 从左边添加元素
d.clear()                           # 清空队列
d.count(3)                          # 统计元素个数
d.extend([2, 4, 5, 3, 1])           # 扩展队列
d.extendleft([9, 8, 0])             # 从左边扩展队列
d.pop()                             # 取出数据并删除
d.popleft()                         # 从左边取出数据并删除
d.remove(9)                         # 删除指定的数据
d.reverse()                         # 翻转队列
d.rotate(3)                         # 旋转容器N步向右，如果N为负数，则向左


from Queue import Queue

q = Queue()
q.put([1, 2, 3, 4])                 # 添加数据
q.get()                             # 从列队移除并返回一个数据
q.empty()                           # 队列如果是空，返回True 否则返会False