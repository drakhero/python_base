from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(("0.0.0.0",3333))

s.listen(5)

coon,addr = s.accept()

f = open("recv.jpg",'wb')

while True:
    data = coon.recv(1014)
    if not data:
        break
    f.write(data)

f.close()
coon.close()
s.close()


