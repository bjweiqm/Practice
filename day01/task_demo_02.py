#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: task_demo_02.py
@time: 2017/4/26 17:33
三级菜单作业
输入b返回上一级菜单
"""


def menu1():
    print '一级菜单'.center(40, '-')
    for k, v in enumerate(dic.keys(), 1):
        print k, v
        dic_keys[str(k)] = v
    choose = raw_input('请输入1级菜单， 输入b返回上一级菜单， 输入q退出菜单：')
    if choose == 'q':
        quit()
    elif choose == 'b':
        print '此处为一级菜单，不能返回'
    elif dic_keys.get(choose):
        menu2(dic_keys[choose])
    else:
        print '输入错误，请重新输入'


def menu2(choose1):
    print '二级菜单'.center(40, '*')
    for k, v in enumerate(dic[choose1].keys(), 1):
        print k, v
        dic_keys[str(k)] = v
    choose2 = raw_input('请输入2级菜单， 输入b返回上一级菜单， 输入q退出菜单：')
    if choose2 == 'q':
        quit()
    elif choose2 == 'b':
        menu1()
    elif dic_keys.get(choose2):
        menu3(choose1, dic_keys[choose2])
    else:
        print '输入错误，请重新输入'
        menu2(choose1)


def menu3(choose1, choose2):
    print '三级菜单'.center(40, '^')
    for k, v in enumerate(dic[choose1][choose2].keys(), 1):
        print k, v
        dic_keys[str(k)] = v
    # for i, y in dic_keys.items():
    #     print i, y, '--'
    choose3 = raw_input('请输入3级菜单， 输入b返回上一级菜单， 输入q退出菜单：')
    if choose3 == 'q':
        quit()
    elif choose3 == 'b':
        menu2(choose2)
    elif dic_keys.get(choose3):
        print dic_keys[choose3]
        menu4(choose1, choose2, dic_keys[choose3])
    else:
        print '输入错误，请重新输入'
        menu3(choose1, choose2)


def menu4(choose1, choose2, choose3):
    print '四级菜单'.center(40, '&')
    for k, v in enumerate(dic[choose1][choose2][choose3], 1):
        print k, v
    choose4 = raw_input('输入b返回上一级菜单， 输入q退出菜单：')
    print len(dic[choose1][choose2][choose3])
    if choose4 == 'b':
        menu3(choose1, choose2)
    elif choose4 == 'q':
        quit()
    elif int(choose4) < len(dic[choose1][choose2][choose3]) + 1:
        print choose1, choose2, choose3, dic[choose1][choose2][choose3][int(choose4)-1]
        quit()
    else:
        print '输入错误，请重新输入'
        menu4(choose1, choose2, choose3)


if __name__ == '__main__':
    dic = {
        "北京": {
            '东城':
                {
                    '沙河': ['老男孩', '恋家'],
                    '天通苑': ['手机卖场', '屌丝吧']
                },
            '朝阳':
                {
                    '花家地': ['朝阳公园', '望京soho'],
                    '北小河': ['北小河公园', '北京中学']
                }
        },
        '上海': {
            '虹桥':
                {
                    '虹桥机场': ['超市', '特产店', '水吧'],
                    '东方明珠': ['电影院', '游泳馆', '餐馆']
                },
            '浦东':
                {
                    '景秀路': ['世纪公园', '立交桥'],
                    '中环路': ['鲁迅公园', '同济大学']
                }
        }
    }
    dic_keys = {}
    # for k, v in enumerate(dic['北京']['东城']['天通苑']):
    #     print k, v
    while True:
        menu1()
