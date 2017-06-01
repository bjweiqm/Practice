#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: socketserver_demo.py
@time: 2017/5/10 10:55
"""

import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print('New Conn: ', self.client_address)
        while True:
            data = self.request.recv(1024)
            if not data: break
            print('client Says: ', str(data, 'utf-8'))
            self.request.send(data)

if __name__ == '__main__':
    HOST, PORT = 'localhost', 50007
    # 把刚才写的一个类当成一个参数传递给ThreadingTCPServer这个类， 下面的代码就创建了一个多线程的socket server
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    # 启动这个server ， 各个server会一直运行，除非按 Crtl-c停止
    server.serve_forever()