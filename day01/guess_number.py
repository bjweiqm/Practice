#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: guess_number.py
@time: 2017/4/27 10:17
猜数字游戏
"""
lucky_num = 19
input_num = -1
guess_count = 0

while guess_count < 3:
    input_num = int(raw_input('input the guess num:'))
    if input_num > lucky_num:
        print '大了...'
    elif input_num < lucky_num:
        print '小了...'
    else:
        print '恭喜...'
        break
    guess_count += 1
else:
    print 'lower'


# for循环实现
for i in range(3):
    input_num = int(raw_input('input the guess num'))
    if input_num > lucky_num:
        print '大了...'
    elif input_num < lucky_num:
        print '小了...'
    else:
        print '恭喜...'
        break
else:
    print 'lower'