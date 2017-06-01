#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: socket_client_demo.py
@time: 2017/5/9 11:25
"""
import socket


ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall(bytes('请占领地球', 'utf-8'))
server_reply = sk.recv(1024)
print(str(server_reply, 'utf-8'))
while True:
    user_input = input('>>: ').strip()
    sk.sendall(bytes(user_input, 'utf-8'))
    server_reply = sk.recv(1024)
    print(str(server_reply, 'utf-8'))
sk.close()