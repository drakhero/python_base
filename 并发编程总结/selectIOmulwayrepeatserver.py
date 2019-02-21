from select import select
from socket import *
import traceback

class Server(object):
    def __init__(self,port):
        self.port = port
        self.createSocket()

    def createSocket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(('',self.port))
        self.sockfd.listen(5)

    def handle(self):
        rlist = [self.sockfd]
        wlist = []
        xlist = []
        while True:
            rs,ws,xs = select(rlist,wlist,xlist)
            for r in rs:
                if r is self.sockfd:
                    try:
                        connfd,addr = r.accept()
                        print("Connect from",addr)
                        rlist.append(connfd)
                    except KeyboardInterrupt:
                        sys.exit("服务器退出")
                    except Exception:
                        traceback.print_exc()
                        sys.exit(0)
                else:

                    data = r.recv(1024)
                    if not data:
                        r.close()
                        rlist.remove(r)
                    else:
                        print(data.decode())
                        wlist.append(r)
            for w in ws:
                w.send(b'Receive')
                wlist.remove(w)


    def serve_forever(self):
        self.handle()


if __name__ == "__main__":
    port = 7777
    server = Server(port)
    server.serve_forever()