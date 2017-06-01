#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: gevent_socket.py
@time: 2017/5/18 21:29
"""
import gevent
from gevent import socket, monkey
monkey.patch_all()


def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)


def handle_request(s):
    try:
        while True:
            data = s.recv(1024)
            print('recv:', data)
            s.send(data)
            if not data:
                s.shutdown(socket.SHUT_WR)

    except Exception as ex:
        print(ex)
    finally:
        s.close()

if __name__ == '__main__':
    server(8001)