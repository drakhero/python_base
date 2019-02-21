# -*- coding:utf-8 -*-

from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)
#host = gethostbyname('tmooc.cn')
#print(host)


server_addr = ('10.8.31.247',9999)
sockfd.connect(server_addr)


while True:
    data = input("发送>>")
    sockfd.send(data.encode())
    sockfd.send("我也来了".encode())
    if data == "##":
        break
    data = sockfd.recv(1024)
    print("recv:",data.decode())


sockfd.close()