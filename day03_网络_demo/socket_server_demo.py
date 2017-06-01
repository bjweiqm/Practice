#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: socket_server_demo.py
@time: 2017/5/9 11:14
"""

import socket


ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('server waiting ...')
    conn, addr = sk.accept()

    client_data = conn.recv(1024)
    print(str(client_data, 'utf-8'))
    conn.sendall(bytes('不要回答， 不要回答, 不要回答', 'utf-8'))
    while True:
        try:
            client_data = conn.recv(1024)
            print(str(client_data, 'utf-8'))
        except Exception:
            print('client closed break ')
            break
        conn.send(client_data)
        # print(str(client_data, 'utf-8'))
        # server_response = input('\033[31;1m>>: \033[0m').strip()
        # conn.send(bytes(server_response, 'utf-8'))
    conn.close()