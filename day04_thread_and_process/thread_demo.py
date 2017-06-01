#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: thread_demo.py
@time: 2017/5/11 11:44
"""
import threading
import time


# 线程锁
def add_num():
    global num
    print('---get num:', num)
    time.sleep(1)
    lock.acquire()
    num -= 1
    lock.release()


lock = threading.Lock()
num = 100
thread_list = []
for i in range(100):
    t = threading.Thread(target=add_num, args=[])
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print('final num:', num)


# 直接调用
# def sayhi(num):
#     print('running on number %s' % num)
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     t_list = []
#     for i in range(10):
#         t = threading.Thread(target=sayhi, args=(i, ))
#         t.start()
#         t_list.append(t)
#
#     for x in t_list:
#         x.join()
#     print('---main---')

    # t1 = threading.Thread(target=sayhi, args=(1, ))
    # t2 = threading.Thread(target=sayhi, args=(2, ))
    #
    # t1.start()
    # t2.start()
    #
    # print(t1.getName())
    # print(t2.getName())
    # t1.join()
    # print('----main----')


# 继承调用
# class MyThread(threading.Thread):
#
#     def __init__(self, num):
#         super(MyThread, self).__init__()
#         self.num = num
#
#     def run(self):
#         print('running on number:%s' % self.num)
#         time.sleep(3)
#
#
# if __name__ == '__main__':
#     my1 = MyThread(1)
#     my2 = MyThread(2)
#
#     my1.start()
#     my2.start()