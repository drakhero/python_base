from socket import *

sockfd = socket()

sockfd.connect(('127.0.0.1',6666))


f = open("img.jpg",'rb')
while True:
    data = f.read(1024)
    if not data:
        break
    sockfd.send(data)



f.close()
sockfd.close()