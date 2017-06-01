#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: run.py
@time: 2017/5/10 21:06
"""
import os
import sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

from core import main

if __name__ == "__main__":
    print(sys.path)
    main.ArvgHandler()