from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)

sockfd.bind(("0.0.0.0",7777))

sockfd.listen(5)

while True:
    print("Write for connect.....")
    connfd, addr = sockfd.accept()


    print("Connect from ",addr)

    while True:
        data = connfd.recv(1024).decode()
        if data == "##":
            break
        print(data)

        n = connfd.send(b'Recerive your message')
        print("发送了",n,"个字节")

    connfd.close()
sockfd.close()



