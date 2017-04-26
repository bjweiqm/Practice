#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: list_demo.py
@time: 2017/4/26 11:10

list 内置方法学习练习
"""


def list_built_in_method_demo():
    """
    summary: python list 内置方法
    :return: None
    """
    # 定义列表元素
    li = list(['zhangsan', 'lisi', 'one', 'zhangsan', 'wang', 'zhao'])
    # 往list内添加数据
    li.append('zhangsan')
    print li
    # 统计元素在列表中出现的次数
    print li.count('zhangsan')
    # 列表后添加另一个列表
    li.extend(['haha', 'hehe'])
    print li
    # 元素第一次出现的位置（索引）,如果没有改元素 报错
    print li.index('one')
    # 接收两个元素， 第一个元素为要插入的位置，第二个为要插入的值
    li.insert(2, 'niuxi')
    print li
    # 删除元素 不给定参数的情况下删除最有一个元素 并返回改元素。给定索引位置的情况下返回该索引的的值，并删除
    print li.pop()
    # 删除指定的的元素
    li.remove('lisi')
    print li
    # 翻转列表中的元素
    li.reverse()
    print li
    # 排序函数， 可接收函数为参数进行排序
    li.sort()
    print li


def list_operation():
    li = (['zhagnsan', 'lisi', 'wangwu', 'zhaoliu', 'qianqi', 'chenba'])
    # list 切片操作
    print li[1:4]
    # list 使用切片达到翻转的效果
    print li[::-1]
    # 依次拿出list中的元素
    for i in li:
        print i
    for i in range(len(li)):
        print li[i]


if __name__ == '__main__':
    list_operation()