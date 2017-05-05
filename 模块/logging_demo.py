#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: logging_demo.py
@time: 2017/5/5 11:45
日志级别：
debug  调试信息
info   正常信息
warning  警告
error   错误
critical  非常严重错误
"""

import logging

# logging.warning('User li attempted wrong password more than 3 times')
# logging.critical('server is down')

# logging 日志写入文件
# logging.basicConfig(
#     filename='test_demo.log',
#     level=logging.INFO,     # 写入到文件中的级别。只写入INFO和他之下的
#     format='%(asctime)s %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S')
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this too')

# ---------------------------------------------------------

# 同时在日志文件和屏幕输出
logger = logging.getLogger('TEST-LOG')  # 生成log对象
logger.setLevel(logging.DEBUG)          # 设置级别 全局的级别 。 全局的优先级最高

# 创建一个对象 负责屏幕打印
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # 设定级别

# 创建一个对象 负责文件
fh = logging.FileHandler('access.log')
fh.setLevel(logging.WARNING)

# 创建格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 把日期格式付给 屏幕 和 文件
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# 把Handler 付给logger
logger.addHandler(ch)
logger.addHandler(fh)


logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')