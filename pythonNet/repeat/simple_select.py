from socket import *
from select import select

server = socket()
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(("0.0.0.0",9999))
server.listen(5)
print("服务器已启动")

rlist = [server]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    print(rs)
    print(ws)
    print("监控到有ＩＯ事件发生")

    for r in rs:
        if r is server:
            client, addr = server.accept()
            print("Connect from:", addr)
            rlist.append(client)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            else:
                print("收到数据",data.decode())
                #wlist.append(r)
    for w in ws:
        pass
    for x in xs:
        pass

server.close()