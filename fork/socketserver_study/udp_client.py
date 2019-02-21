#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from socket import  *
import sys

if len(sys.argv) < 3:
    print('''
        argv is error!
        run as
        python3 udp_client.py 127.0.0.1 8888
    ''')

    raise


#从命令行输入IP,端口
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input("消息：")
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(1024)
    print("从服务器收到：",data.decode())
sockfd.close()