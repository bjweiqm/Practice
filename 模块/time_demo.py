#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: time_demo.py
@time: 2017/5/3 17:31
"""

# 时间模块

import time


# 返回处理器时间， 3.3开始废弃
print(time.clock())
print(time.altzone)             # 返回与utc时间的时间差,以秒计算
print(time.asctime())           # 返回时间格式"Fri Aug 19 11:14:16 2016"
# 返回处理器时间， 3,3 开始已废弃
print(time.process_time())
# 返回当前系统时间戳
print(time.time())
# 输出 Wed May  3 17:34:43 2017， 当前系统时间
print(time.ctime())
# 将时间戳转为字符串格式
print(time.ctime(time.time()))
# 将时间戳转换成 struct_time格式
print(time.gmtime(time.time()))
# 将时间戳转成struct_time格式 但返回的本地时间
print(time.localtime(time.time()))
# 与time。localtime()功能相反， 翻转成时间戳格式
print(time.mktime(time.localtime()))
# 将struct_time格式转换成指定的字符串格式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
# 将字符串转换成 struct_tiem格式
print(time.strptime("2016-01-28", "%Y-%m-%d"))


# ----------------------------------------------------------------------------------------------------------------
import datetime

print(datetime.datetime.now())                      # 返回 2016-08-19 12:47:03.941925
print(datetime.datetime.today())                    # 返回 2016-08-19 12:47:03.941925
print(datetime.date.fromtimestamp(time.time()))     # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now() + datetime.timedelta(3))              # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))             # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))        # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))     # 当前时间+30分
print(datetime.datetime.today())
