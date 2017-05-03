#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: 计算器_demo.py
@time: 2017/5/2 18:03

实现加减乘除及拓号优先级解析
用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式，运算后得出结果，结果必须与真实的计算器所得出的结果一致

"""

import re


def mutilpy_and_dividend(formula):
    print('运算', formula)
    calc_list = re.split("[+-]", formula)
    print(calc_list)
    return 'None'


def calc(formula):
    parentheses_flag = True
    while parentheses_flag:
        m = re.search('\([^()]+\)', formula)
        if m:
            print(m.group())
            sub_formula = m.group().strip('()')
            sub_res = mutilpy_and_dividend(sub_formula)
        break


if __name__ == '__main__':
    formula = "1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ) * (-40/5)) - (-4*3)/ (16-3*2) )"
    calc(formula)