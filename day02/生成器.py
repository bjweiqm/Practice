#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 生成器.py
@time: 2017/4/30 17:38
"""

"""
# 迭代器 访问元素的一种方式 只能前进不能后退
name = iter(['zhang', 'zhao', 'wang', 'ma'])
# Python2 实现方式
# print(name.next())
# print(name.next())
# print(name.next())
# print(name.next())
# python 3
print(name.__next__())
print(name.__next__())
print(name.__next__())
print(name.__next__())
# 越界的话报 StopIteration 异常
print(name.__next__())

"""


# 如果一个函数返回的是一个迭代器，那么这个函数叫做生成器
def cash_money(amount):
    while amount > 0:
        amount -= 100
        yield 100
        print('又来取钱了!')

# atm = cash_money(500)
# print(atm.__next__())
# print(atm.__next__())

# 迭代器异步
import time


def consumer(name):
    print('%s 要准备吃包子!' % name)
    while True:
        baozi = yield
        print('包子[%s] 来了， 被[%s] is 吃了！' % (baozi, name))


def producer(name):
    c = consumer('A')
    b = consumer('B')
    c.__next__()
    b.__next__()
    print('%s 准备开始做包子了' % name)
    for i in range(10):
        time.sleep(1)
        print('做了两个包子')
        c.send(i)       # 给生成器传递信息
        b.send(i)

producer('zhang')