#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 函数.py
@time: 2017/4/30 13:31
"""


# 定义函数
def ab():
    print 'ab'

# 调用函数
ab()


# 返回值
def aoe():
    return 'wagaae'
aoe()


# 带参函数
def abc(name):
    print(name)


# 带默认参数函数
def abcs(name='youcai'):
    if name == 'youcai':
        print('name')
    else:
        print('meicai')


# 指定参数
def show(a, b):
    print(a, b)

# 调用
show(b=23, a=20)


# 动态参数
def dong(*args):
    print(args)          # args类型为tuple

dong(1, 2, 3, 4, 5)


def dong1(**kwargs):
    print(kwargs)        # kwargs类型为dict


def dong2(*args, **kwargs):     # 传入参数必须后传指定参数
    print(args)
    print(kwargs)
# 三种传参方式
dong2(1, 2, 3, name='zhangsan', age=30, job='gan')
dong2(*[1, 2, 3], **{'name': 'zhangsan', 'age': 30, 'job': 'nong'})
a = [1, 2, 3]
b = {'name': 'zhangsan', 'age': 30, 'job': 'nong'}
dong2(*a, **b)


# lambda 表达式
def func(a):
    a += 1
    return a

func1 = lambda a: a+1
print(func1(99))
