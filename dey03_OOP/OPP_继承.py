#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: OPP_继承.py
@time: 2017/5/8 15:10
"""


class SchoolMember(object):
    member = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        SchoolMember.member += 1
        print('\033[32;1mThe [%s] SchoolMember [%s] is enrolled! \033[0m' % (self.member, self.name))

    def tell(self):
        print('Hello my name is %s ' % self.name)


class Teacher(SchoolMember):

    def __init__(self, name, age, sex, sourse, salary):
        super(Teacher, self).__init__(name, age, sex)       # 继承父类的构造方法
        # SchoolMember.__init__(self, name, age, sex)       # 经典类实现方法
        self.sourse = sourse
        self.salary = salary

    def teaching(self):
        print('Teacher [%s] is teaching [%s]' % (self.name, self.sourse))


class Student(SchoolMember):

    def __init__(self, name, age, sex, course, tuition):
        super(Student, self).__init__(name, age, sex)
        self.couser = course
        self.tuition = tuition

    def pay_tution(self):
        print('cao, [%s] paying tution [%s]' % (self.name, self.tuition))


if __name__ == '__main__':
    t1 = Teacher('alex', 22, 'F', 'PY', '1000')
    t2 = Teacher('tenglan', 25, 'N/A', 'PY', '900')
    s1 = Student('San', 24, 'Female', 'python', 15000)
    s2 = Student('BaoAn', 23, 'F', 'python', 5000)

    t1.teaching()
    s1.pay_tution()