#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: select_soket.py
@time: 2017/5/19 0:32
"""

import select
import socket
import sys
import queue


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
server.bind(server_address)
server.listen(5)

inputs = [server]
outputs = []
