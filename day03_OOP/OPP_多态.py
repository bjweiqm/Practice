#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: OPP_多态.py
@time: 2017/5/8 16:32
"""


"""
class Animal(object):

    def __init__(self, name):
        self.name = name

    def talk(self):
        raise 'Talk Error'


class Cat(Animal):

    def talk(self):
        return 'Meow!'


class Dog(Animal):

    def talk(self):
        return 'Woof! Woof!'


def animal_talk(obj):
    print(obj.talk())


c = Cat('SanJiangMei')
d = Dog('SanJiangYuan')
animal_talk(c)
animal_talk(d)

# animals = [Cat('Missy'), Dog('Lassie')]
#
# for animal in animals:
#     print(animal.name + ':' + animal.talk())

"""