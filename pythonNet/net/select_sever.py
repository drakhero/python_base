from select import select
from socket import *

#创建套接字作为我们关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',7777))
s.listen(2)

rlist = [s]
wlist = []
xlist = []

#提交监测我们关注的ＩＯ，等待ＩＯ发生
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr =r.accept()
            print("Connect from",addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                wlist.append(r)
    for w in ws:
        w.send(b'Receive your message')
        wlist.remove(w)

