from socket import *
import  struct

adress = ("0.0.0.0",9999)
server = socket(AF_INET,SOCK_DGRAM)
server.bind(adress)

while True:
    data,addr = server.recvfrom(1024)
    fmt = data.decode()
    data,addr = server.recvfrom(1024)
    msg = struct.unpack(fmt,data)

    print(msg[1].decode())
server.close()