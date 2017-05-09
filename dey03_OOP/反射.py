#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 反射.py
@time: 2017/5/9 9:53
"""

import sys


class WebServer(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        print('Server is starting ...')

    def stop(self):
        print('Server is stipping ...')

    def restart(self):
        self.stop()
        self.start()


def test_run(cls, name):
    print('runing... ', name, cls.host)


if __name__ == '__main__':
    web = WebServer('localhost', 3333)
    # 判断属性是否存在
    if hasattr(web, sys.argv[1]):
        # 获取属性的内存地址
        func = getattr(web, sys.argv[1])   # 获取web.start 内存地址
        func()  # func() == web.start()
    # 添加对象 方法
    setattr(web, 'run', test_run)
    web.run(web, 'alex')
    delattr(web, 'restart')

    # print(sys.argv[1])
    # 一级版本
    # if sys.argv[1] == 'start':
    #     web.start()

    # 二级版本
    # dic = {
    #     'start': web.start,
    #     'stop': web.start,
    #     'restart': web.restart
    # }
    # if sys.argv[1] in dic:
    #     dic[sys.argv[1]]()