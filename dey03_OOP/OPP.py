#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: OPP.py
@time: 2017/5/8 17:02
"""


class Animal(object):
    hobbie = 'meat'

    def __init__(self, name):
        # 构造方法 ， 调用类是自动执行
        self.name = name
        self.num = None

    @classmethod
    def talk(cls):     # 类方法  不能访问实例变量
        print('%s is talking...' % cls.hobbie)

    @staticmethod
    def walk():     # 静态方法   不能访问实例变量 和 类变量
        print('%s is walking...')

    @property
    def habit(self):       # 方法变成属性
        print('%s habit is haha' % self.name)

    @habit.setter
    def habit(self, num):       # 方法变成属性
        self.num = num
        print('total players: %s' % self.num)

    @habit.deleter
    def habit(self):       # 方法变成属性
        print('habit player got delete.')

    def __del__(self):
        # 析构方法 当内存被释放时触发。
        pass


if __name__ == '__main__':
    # d = Animal('SanMao')
    # Animal.talk()
    # d.walk()
    # d.habit
    a = Animal('SanMao')
    print(a.habit)
    a.habit = 3
    # a.__doc__         # 获取注释
    # a.__module__      # 表示当前操作的对象在那个模块
    # a.__class__       # 表示当前操作的对象的类是什么


    del a.habit