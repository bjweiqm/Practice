#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: re_demo.py
@time: 2017/5/2 18:07
"""

import re


data = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

# 生成要匹配的正则对象
p = re.compile('\d+')
# 从头开始匹配
s = re.match('\d', data)
#
s = re.search('\d{3}', data)


if __name__ == '__main__':
    if s:
        print(s.group())
