from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)

server_addr = ("127.0.0.1",9999)
sockfd.connect(server_addr)

while True:
    try:
        data = input("发送>>")
        sockfd.send(data.encode())
    except InterruptedError:
        sockfd.close()


    print("**********")
    # data = sockfd.recv(1024).decode()
    # print("接收到:",data)

#sockfd.close()



