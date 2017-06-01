#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: socket_client_ssh_demo.py
@time: 2017/5/9 15:43
"""

import socket


ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)

while True:
    user_input = input('cmd:').strip()
    if len(user_input) == 0: continue
    if user_input == 'q': break

    sk.send(bytes(user_input, 'utf-8'))
    server_ack_msg = sk.recv(100)
    cmd_res_msg = str(server_ack_msg, 'gbk').split("|")
    print(cmd_res_msg)
    if cmd_res_msg[0] == "Cmd_result_size":
        cmd_res_size = int(cmd_res_msg[1])
        sk.send(b'CLIENT_READY_TO_RECV')

    res = ''
    received_size = 0
    while received_size < cmd_res_size:
        data = sk.recv(500)
        received_size += len(data)
        res += str(data, 'gbk')
    else:
        print(res)
        print('---recv down---')
        # server_replay = sk.recv(500)
        # res += str(server_replay, 'gbk')
        # # print(str(server_replay, 'gbk'))
        # if len(server_replay) < 500:
        #     print(res)
        #     print("------last time-------")
        #     break
    # sk.sendall(bytes(user_input, 'utf-8'))
    # server_reply = sk.recv(1024)
    # try:
    #     print(str(server_reply, 'utf-8'))
    # except UnicodeDecodeError as e:
    #     print(str(server_reply, 'gbk'))

sk.close()