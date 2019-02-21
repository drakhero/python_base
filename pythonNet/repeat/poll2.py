from socket import *
from select import *

server = socket()
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
addr = ("0.0.0.0",9999)
server.bind(addr)
server.listen(5)
print("服务器已连接")

fdmap = {
    server.fileno() : server
}

p = poll()
p.register(server,POLLIN)

while True:
    events = p.poll()
    print(events)
    for fd,e in events:
        sock = fdmap[fd]
        if fd == server.fileno():
            client,addr = sock.accept()
            print("已连接到",addr)
            p.register(client,POLLIN)
            fdmap[client.fileno()] = client

        elif e & POLLIN:
            print("here")
            try:
                data = sock.recv(1024)
                print(data.decode())

            except Exception as e:
                print("客户端断开",e)
                p.unregister(sock)
                sock.close()
                fdmap.pop(fd)
                continue

            if not data:
                print("客户端断开")
                p.unregister(sock)
                sock.close()
                fdmap.pop(fd)
            else:
                print("收到数据:",data.decode())
                sock.send(b"hello")
        else:
            print("对方退出")

