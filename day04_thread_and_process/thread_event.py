#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: thread_event.py
@time: 2017/5/11 14:41
"""

import time
import threading
import random


def light():
    if event.isSet():
        event.set()
    count = 0
    while True:
        if count < 10:
            print('绿灯')
        elif count < 13:
            print('红灯')
        elif count < 20:
            if event.isSet():
                event.clear()
            print('red light on')
        else:
            count = 0
            event.set()
        time.sleep(1)
        count += 1


def car(n):
    while 1:
        time.sleep(1)
        if event.isSet():
            print('car [%s] is running..' % n)
        else:
            print('car [%s] is waiting for the red light..' % n)
            event.wait()
    # while 1:
    #     time.sleep(random.randrange(10))
    #     if event.isSet():
    #         print('car [%s] is running..' % n)
    #     else:
    #         print('car [%s] is waiting for the red light..' % n)


if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car, args=[i, ])
        t.start()