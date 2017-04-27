#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: str_demo.py
@time: 2017/4/27 17:52
"""


"""
'''字符串格式输出对齐'''
# format()
print '{0}, {1}, {2}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format(*'abc')
print 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print 'Coordinates: {latitude}, {longitude}'.format(**coord)


str = 'stRINg lEArn'

print str.center(20)                             # 生成20个字符长度，str排中间
print str.ljust(20)                              # str左对齐
print str.rjust(20)                              # str右对齐
print str.zfill(20)                              # str右对齐，左边填充0



'''大小写转换'''
str = 'stRINg lEArn'

print str.lower()                              # 转小写
print str.upper()                              # 转大写
print str.capitalize()                         # 首字母大写，其余小写
print str.swapcase()                           # 大小写对换
print str.title()                              # 以分隔符为标记，首字母大写，其余小写



'''字符串条件判断'''
str = '0123'

print str.isalnum()                             # 是否全是字母和数字
print str.isdigit()                             # 是否全是数字
print str.islower()                             # 是否全是小写，当全是小写和数字一起的时候，也判断为True
print str.isupper()                             # 是否全是大写，当全是大写和数字一起的时候，也判断为True
print str.isspace()                             # 是否全是空白字符
print str.istitle()                             # 所有单词字首都是大写，标题
print str.startswith('0')                       # 判断字符串以'0'开头
print str.endswith('0')                         # 判读字符串以'0'结尾



'''字符串搜索定位与替换'''

str = 'string lEARn'
print str.find('a')                              # 查找字符串，没有则返回-1，有则返回查到到第一个匹配的索引
print str.rfind('n')                             # 返回的索引最后一次的匹配
print str.index('n')                             # 同find类似,返回第一次匹配的索引值，如果没有找到就报错
print str.rindex('n')                            # 返回最后一次匹配的索引值，如果没有找到就报错
print str.count('n')                             # 字符串中匹配的次数
print str.replace('EAR', 'ear')                  # 匹配替换
print str.strip('n')                             # 删除字符串首尾匹配的字符，通常用于默认删除回车符
print str.lstrip('s')                            # 左匹配
print str.rstrip('n')                            # 右匹配
str = ' abc'
print str.expandtabs()                           # 把制表符转为空格
print str.expandtabs(2)                          # 指定空格数




'''字符串编码与解码'''

str = '学习字符串'

print str.decode('utf-8')                        # 字符串解码，将utf-8解码成unicode
print str.decode('utf-8').encode('gbk')          # 先解码，在编码，把Unicode编码成gbk
print unicode(str, 'utf-8').encode('gbk')        # 先解码，在编码，把Unicode编码成gbk
"""


import string
# print dir(string)

"""
funOrC = []
va = []
for fv in dir(string):
    name = 'string.%s' % fv
    if callable(eval(name)):
        funOrC.append(fv)
    else:
        va.append(fv)

''' string 方法中常量
('_re', '====>', <module 're' from 'C:\Python25\lib\re.pyc'>)
('ascii_letters', '====>', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
('ascii_lowercase', '====>', 'abcdefghijklmnopqrstuvwxyz')
('ascii_uppercase', '====>', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
('digits', '====>', '0123456789')
('hexdigits', '====>', '0123456789abcdefABCDEF')
('letters', '====>', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
('lowercase', '====>', 'abcdefghijklmnopqrstuvwxyz')
('octdigits', '====>', '01234567')
('printable', '====>', '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c')
('punctuation', '====>', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
('uppercase', '====>', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
('whitespace', '====>', '\t\n\x0b\x0c\r ')
'''

for v in va:
    print v, '====>', eval('string.%s' % v)

"""

'''
s = 'hell world'

print string.capitalize(s)                              # 返回一个字符串副本，首字母大写
print string.capwords(s)                                # 每个单词的首字母大写
print string.center(s, 50, '-')                         # string.center(s, width[, fillchar])函数，用指定的宽度来返回一个居中版的s，如果需要的话，就用fillchar进行填充，默认是空格。但是不会对s进行截取。即如果s的长度比width大，也不会对s进行截取。
print string.count(s, 'l')                              # string.count(s,sub[,start[,end]])返回在s[start:end]范围内子串sub在字符串s当中出现的次数
print string.find(s, 'a')                               # string.find(s,sub[,start[,end]])返回在s[start:end]范围内子串sub在字符串s当中出现的最小下标，没有找到返回-1
print string.index(s, 'l')                              # string.index(s,sub[,start[,end]])与string.find方法类似，只不过当没有找到子串sub的时候，会抛出ValueError异常

# ************** string 同上方一致 **************

'''