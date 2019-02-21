from socket import *

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定服务端地址
sever_addr = ("0.0.0.0",8888)
sockfd.bind(sever_addr)

#消息收发
while True:
    data,addr = sockfd.recvfrom(1024)
    if not data:
        break
    print("Receive from %s:%s"%(addr,data.decode()))

    sockfd.sendto("收到你的消息".encode(),addr)

sockfd.close()