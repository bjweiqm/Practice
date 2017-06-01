#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: socetserver_client_demo.py
@time: 2017/5/10 11:09
"""
import socket


ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.connect(ip_port)
while True:
    user_input = input('>>: ').strip()
    sk.sendall(bytes(user_input, 'utf-8'))
    server_reply = sk.recv(1024)
    print(str(server_reply, 'utf-8'))
sk.close()