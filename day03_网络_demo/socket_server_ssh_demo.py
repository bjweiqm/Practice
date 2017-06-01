#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: socket_server_ssh_demo.py
@time: 2017/5/9 15:35
"""
import time
import socket
import subprocess

ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.bind(ip_port)  # 绑定IP地址和端口号
sk.listen(5)      # 指定在拒绝链接之前可以挂起的最大连接数量

while True:
    print('server waiting ...')
    conn, addr = sk.accept()    # 接收返回；

    while True:
        client_data = conn.recv(1024)
        if not client_data:
            break
        print('recv >>', str(client_data, 'utf-8'))
        cmd = str(client_data, 'utf-8').strip()
        cmd_call = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        cmd_result = cmd_call.stdout.read()
        if len(cmd_result) == 0:
            cmd_result = b'cmd execution has no output...'
        ack_msg = bytes('Cmd_result_size|%s' % len(cmd_result), 'utf-8')
        conn.send(ack_msg)
        # 解决 黏包问题 让客户端确认收数据
        client_ack = conn.recv(10)
        if str(client_ack, 'utf-8') == 'CLIENT_READY_TO_RECV':
            conn.send(cmd_result)
    conn.close()
