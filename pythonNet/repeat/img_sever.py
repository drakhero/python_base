from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)

sockfd.bind(("0.0.0.0",6666))
sockfd.listen(5)

c,addr = sockfd.accept()
f = open("get.jpg",'wb')

while True:
    data = c.recv(1014)
    print(data)
    if not data:
        break

    f.write(data)
f.close()
c.close()
sockfd.close()

