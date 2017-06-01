#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: yield.py
@time: 2017/5/18 17:53
"""

import time
import queue


def consumer(name):
    print('---> starting eating baozi....')
    while True:
        new_baozi = yield
        print('[%s] is eating baozi %s ' % (name, new_baozi))


def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0

    while n < 5:
        n += 1
        con.send(n)
        con2.send(n)
        print('[producer] is making baozi %s' % n)


if __name__ == '__main__':
    con = consumer('c1')
    con2 = consumer('c2')
    p = producer()