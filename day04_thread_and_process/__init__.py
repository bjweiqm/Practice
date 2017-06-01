#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: __init__.py.py
@time: 2017/5/11 10:12
1. 线程继承在进程中
2. 进程启动速度比线程启动速度快（进程启动要先申请内存）
"""

import time
import threading


def run(n):
    print('[%s] --running--\n' % n)
    time.sleep(2)
    print('--done--')


def main():
    for i in range(5):
        t = threading.Thread(target=run, args=[i, ])
        t.start()
        print('starting thread', t.getName())


m = threading.Thread(target=main)
# m.setDaemon(True)  # 将主线程设置为Daemon线程， 他退出时， 其它子线程也退出
m.start()
m.join(timeout=3)  # 设置timeout后 就不阻塞了。
print('---mian thread done---')