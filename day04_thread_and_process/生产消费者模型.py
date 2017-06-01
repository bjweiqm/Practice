#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 生产消费者模型.py
@time: 2017/5/18 15:03
"""

import threading
import queue
import time


def consumer(n):
    # 消费
    print('consume [%s] get task: %s' % (n, q.get()))
    q.task_done()


def producer(n):
    # 生产
    count = 1
    while True:
        time.sleep(0.5)
        print('prodcer [%s] produced a new task: %s' % (n, count))
        q.put(count)
        count += 1
        q.join()
        print('all taks has been cosumed by consumers...')


q = queue.Queue(maxsize=30)

c1 = threading.Thread(target=consumer, args=(1,))
c2 = threading.Thread(target=consumer, args=(2,))
c3 = threading.Thread(target=consumer, args=(3,))

p = threading.Thread(target=producer, args=('zhang',))
p1 = threading.Thread(target=producer, args=('wang',))

c1.start()
c2.start()
c3.start()
p.start()
p1.start()
