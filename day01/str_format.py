#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: str_format.py
@time: 2017/4/27 11:23
参数介绍：

c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
o，将整数转换成 八  进制表示，并将其格式化到指定位置
x，将整数转换成十六进制表示，并将其格式化到指定位置
d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
F，同上
g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）


format([[fill]align][sign][#][0][width][,][.precision][type])
    fill         【可选】空白处填充的字符

    align        【可选】对齐方式（需配合width使用）
        <，内容左对齐
        >，内容右对齐(默认)
        ＝，内容右对齐，将符号放置在填充字符的左侧，且只对数字类型有效。即使：符号+填充物+数字
        ^，内容居中

    sign         【可选】有无符号数字
        +，正号加正，负号加负；
        -，正号不变，负号加负；
        空格 ，正号空格，负号加负；

    #            【可选】对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示

    ，           【可选】为数字添加分隔符，如：1,000,000
    width        【可选】格式化位所占宽度
    .precision   【可选】小数位保留精度

    type         【可选】格式化类型
        传入” 字符串类型 “的参数
            s，格式化字符串类型数据
            空白，未指定类型，则默认是None，同s
        传入“ 整数类型 ”的参数
            b，将10进制整数自动转换成2进制表示然后格式化
            c，将10进制整数自动转换为其对应的unicode字符
            d，十进制整数
            o，将10进制整数自动转换成8进制表示然后格式化；
            x，将10进制整数自动转换成16进制表示然后格式化（小写x）
            X，将10进制整数自动转换成16进制表示然后格式化（大写X）
        传入“ 浮点型或小数类型 ”的参数
            e， 转换为科学计数法（小写e）表示，然后格式化；
            E， 转换为科学计数法（大写E）表示，然后格式化;
            f， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
            F， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
            g， 自动在e和f中切换
            G， 自动在E和F中切换
            %，显示百分比（默认显示小数点后6位）
"""


# % 方式
print "Infomating of [%s]: \nname:%s \nage:%d \njob:%s " % ('zhangsan', 'zhangsan', 19, 'kaifa')
print "i am %s" % "alex"
print "i am %s age %d" % ("alex", 18)               # %d 只能接受数字
print "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
print "percent %.2f" % 99.97623    # 打印浮点数
print "i am %(pp).2f" % {"pp": 123.425556, }
print "i am %(pp).2f %%" % {"pp": 123.425556, }     # 打印百分比
print 'i am %s my hobby is %s' % ('lhf', 1)         # %s可以接受任意参数

# format() 方式：
print "i am {}, age {}, {}".format("seven", 18, 'alex')
print "i am {}, age {}, {}".format(*["seven", 18, 'alex'])  # 必须一一对应，否则会报错
print "i am {0}, age {1}, really {0}".format("seven", 18)
print "i am {0}, age {1}, really {0}".format(*["seven", 18])
print "i am {name}, age {age}, really {name}".format(name="seven", age=18)
print "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})    # ** 代表传字典
print "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
print "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)    # s 代表字符串 d 代表整数
print "i am {:s}, age {:d}".format(*["seven", 18])  # * 代表列表
print "i am {name:s}, age {age:d}".format(name="seven", age=18)
print "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
print "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)  # 2进制 8进制 10进制  x与X: 16进制 %：百分比
print "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
print "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)