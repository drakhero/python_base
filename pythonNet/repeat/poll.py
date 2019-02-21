from socket import *
from select import *

address = ("0.0.0.0",9999)
server = socket()
server.bind(address)
server.listen(5)
print("服务器已启动！！！", address)

fdmap = {
    server.fileno() : server
}

p = poll()
p.register(server,POLLIN)

while True:

    events = p.poll()
    for fd,e in events:
        sock = fdmap[fd]
        if fd == server.fileno():
            client,addr = server.accept()
            print("收到连接")
            p.register(client,POLLIN)
            fdmap[client.fileno()] = client
        elif e & POLLIN:
            data = sock.recv(1024)
            print(data)
            if not data:
                p.unregister(fd)
                sock.close()
                del fdmap[fd]
            else:
                print("收到数据:",data.decode())
                sock.send(b"test msg")




