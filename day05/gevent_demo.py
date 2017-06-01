#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: gevent_demo.py
@time: 2017/5/18 18:15
依赖三方库 gevent
"""

import gevent


def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)
])