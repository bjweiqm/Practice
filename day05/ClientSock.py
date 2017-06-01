#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: ClientSock.py
@time: 2017/5/18 21:42
"""


import socket


HOST = 'localhost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = bytes(input('>>: ').strip(), encoding='utf-8')
    if len(msg) == 0: continue
    s.sendall(msg)
    data = s.recv(1024)
    print('Received', repr(data))

s.close()