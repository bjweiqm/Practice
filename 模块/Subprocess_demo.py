#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: Subprocess_demo.py
@time: 2017/5/5 11:15
打算 替换掉
os.system
os.spawn*
"""

import os
import subprocess

a = subprocess.run('ipconfig')
# print([x for x in dir(a) if not x.startswith("_")])
# print(a.args)
# print(a.stderr)
# print(a.stdout)
# print(a.returncode)
# print(a.check_returncode)

