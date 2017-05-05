#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: config_parser_demo.py
@time: 2017/5/4 18:35
"""
import configparser

config = configparser.ConfigParser()


def write_demo():
    config['DEFAULT'] = {
        'ServerAliveInterval': '45',
        'Compression': 'yes',
        'CompressionLevel': '9'
    }
    # 生成接点
    config['bitbucket.org'] = {}
    # 往接点中写入数据
    config['bitbucket.org']['User'] = 'hg'
    # 生成接点
    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']

    topsecret['Host Port'] = '50022'
    topsecret['ForwardX11'] = 'no'

    config['DEFAULT']['ForwardX11'] = 'yes'

    with open('example.ini', 'w') as configfile:
        config.write(configfile)


def read_demo():
    # 读取文件
    config.read('example.ini')
    # 读取 DEFAULT 里面的值（全局变量）
    print(config.defaults())

    # 获取全部接点
    con = config.sections()
    print(con)

    print(config['bitbucket.org']['User'])

    for key in config['bitbucket.org']:
        print(key)

    # options(key) 取出key中所有的数据
    print(config.options('bitbucket.org'))

    print(config.get('bitbucket.org', 'User'))


def change_demo():
    config.read('example.ini')


def del_demo():
    config.read('example.ini')
    config.remove_section('bitbucket.org')
    config.write(open('example2.ini', 'w'))


def judge_demo():   # 判断
    config.read('example.ini')
    # 判断有没有 laowang 这个 接点
    sec = config.has_section('laowang')
    # 添加接点
    config.add_section("laowang")
    print(sec)
    config['laowang']['age'] = '12'
    config['laowang']['job'] = 'IT Python'
    config.write(open('example2.ini', 'w'))
    # 修改 wupeiqi接点下的 age
    config.set('laowang', 'age', '22')
    config.write(open('example3.ini', 'w'))
    # 删除 laowang 节点下 age元素
    config.remove_option('laowang', 'age')
    config.write(open('example3.ini', 'w'))


if __name__ == '__main__':
    # read_demo()
    # del_demo()
    judge_demo()