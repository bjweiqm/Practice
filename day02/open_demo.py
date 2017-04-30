#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: open_demo.py
@time: 2017/4/30 15:24

打开文件的模式有：

    r，只读模式（默认）。
    w，只写模式。【不可读；不存在则创建；存在则删除内容；】
    a，追加模式。【可读；   不存在则创建；存在则只追加内容；】

"+" 表示可以同时读写某个文件

    r+，可读写文件。【可读；可写；可追加】
    w+，写读
    a+，同a

"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

    rU
    r+U

"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

    rb
    wb
    ab

"""
