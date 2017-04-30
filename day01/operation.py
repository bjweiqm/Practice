#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: operation.py
@time: 2017/4/27 18:39
运算符：
and	| x and y	| 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 	 | (a and b) 返回 20。
or	| x or y	| 布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	         | (a or b) 返回 10。
not	| not x	    | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	 | not(a and b) 返回 False

"""

a = 10
b = 20

if a and b:
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if a and b:
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not a:
    print("5 - 变量 a 为 false")
else:
    print("5 - 变量 a 为 true")


"""
in	    | 如果在指定的序列中找到值返回 True，否则返回 False。 	    | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	| 如果在指定的序列中没有找到值返回 True，否则返回 False。 	| x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
"""

a = 10
b = 20
lis = [1, 2, 3, 4, 5]

if a in lis:
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if b not in lis:
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if a in lis:
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")


"""
is	    | is是判断两个标识符是不是引用自一个对象	    | x is y, 如果 id(x) 等于 id(y) , is 返回结果 1
is not	| is not是判断两个标识符是不是引用自不同对象	| x is not y, 如果 id(x) 不等于 id(y). is not 返回结果 1
"""

a = 20
b = 20

if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if id(a) is not id(b):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")