from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#绑定地址
sockfd.bind(("0.0.0.0",9998))

#设置监听
sockfd.listen(5)

#等待接受连接
while True:
    print("Writing for connect....")
    connfd,addr = sockfd.accept()
    print("Connect from",addr)

    #收发消息
    while True:
        data = connfd.recv(1024).decode()
        if data == "##":
            break
        print(data)
        n = connfd.send(b'Receive your message')
        print("你发送了",n,"个字节")

#关闭套接字
    connfd.close()
sockfd.close()