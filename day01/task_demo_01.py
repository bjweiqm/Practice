#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: task_demo_01.py
@time: 2017/4/26 11:11
1. 用户登录
2. 输入密码错误3次锁死
"""


def read_user_file():
    # 获取用户信息文件
    with file('task_demo_01', 'rb') as fb:
        li = fb.read()
        return eval(li)


def login(user):
    blink = user[-1]
    while True:
        name = raw_input('name: ')
        pwd = raw_input('passwd: ')
        # 判断用户密码输入错误次数
        if blink < 2:
            if name == user[0] and pwd == user[1]:
                print('welcome %s' % user[0])
                break
            else:
                blink += 1
        else:
            user[-1] = blink
            # 存储 用户信息（输入错误三次后执行）
            with file('task_demo_01', 'wb') as fb:
                fb.write('["%s", "%s", %d]' % tuple(user))
            print('lock is %s' % user[0])
            break


if __name__ == '__main__':
    user = read_user_file()
    login(user)
