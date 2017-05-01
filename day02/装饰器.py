#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 装饰器.py
@time: 2017/4/30 18:59
"""

# --------------------------------------------------基本装饰器----------------------------------------------------------


def login(func):
    def inner(*args, **kwargs):                 # 内置方法，保证调用方法是才会被执行
        print('断言登录操作')
        return func(*args)                      # 被装饰的方法需要有返回值，需要返回改方法
    return inner


# 执行 login， 把自己装饰的函数的函数名当参数，login(tv)
# tv 函数重新定义，定义为login的返回值
# 新的tv函数等于 inner
@login
def tv(name):
    print('%s to TV page' % name)
    return name                                 # 添加返回值


def moive(name):
    print('%s to Moive page' % name)

# tv('zhao')
# print(tv('zhao'))

# ------------------------------------------------给装饰器添加参数-------------------------------------------------------


def logins(request, kargs):
    print('before')


def error_handle(request, kargs):
    print('after')


def filter_demo(before_func, after_func):
    def outer(main_func):
        def wrapper(request, kargs):
            before_result = before_func(request, kargs)
            if before_result is not None:
                return before_result

            main_result = main_func(request, kargs)
            if main_result is not None:
                return main_result

            after_result = after_func(request,kargs)
            if after_result is not None:
                return after_result

        return wrapper
    return outer


@filter_demo(logins, error_handle)
def index(request, kargs):
    print('index')

index('req', 'zhao')