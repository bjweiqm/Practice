#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: hashlib_demo.py
@time: 2017/5/5 10:41
加密相关的操作
"""

import hashlib

a = hashlib.md5()
print([di for di in dir(a) if not str(di).startswith("_")])
a.update(b"Hello")
a.update(b'It`s me')
# 二进制
print(a.digest())
# 十六进制
print(a.hexdigest())

b = hashlib.sha512()
b.update(b'Hello')
print(b.digest())
print(b.hexdigest())