#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: opp_封装.py
@time: 2017/5/8 10:04
"""


class Role(object):
    ac = None  # 类变量、类属性

    def __init__(self, name, role, weapon, life_value):
        self.name = name    # 成员变量
        self.role = role
        self.weapon = weapon
        self.life_value = life_value

    def buy_weapon(self, weapon):
        print('%s is buying [%s]' % (self.name, weapon))
        self.weapon = weapon


if __name__ == '__main__':
    r = Role('San', 'Police', 'B10', 90)
    r1 = Role('Chun', 'Terrorist', 'B11', 100)
    r.buy_weapon('AK47')
    r1.buy_weapon('B51')
    print('r:', r.weapon)
    print('r1:', r1.weapon)