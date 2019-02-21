from socket import *
from select import *
import traceback
import sys

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
        p = epoll()
        fdmap = {self.sockfd.fileno():self.sockfd}
        p.register(self.sockfd,POLLIN | POLLERR)

        while True:
            events = p.poll()
            for fd,event in events:
                if fd == self.sockfd.fileno():
                    try:
                        connfd,addr = fdmap[fd].accept()
                        print("Connect from",addr)
                    except InterruptedError:
                        sys.exit("服务器退出")
                    except Exception:
                        traceback.print_exc()
                        sys.exit(0)
                    p.register(connfd,EPOLLIN | EPOLLOUT)
                    fdmap[connfd.fileno()] = connfd

                elif event & EPOLLIN:
                    try:
                        data = fdmap[fd].recv(1024)
                    except:
                        p.unregister(fd)
                        fdmap[fd].close()
                        del fdmap[fd]
                        print("客户端退出")
                        continue
                    #p.register(fd,EPOLLOUT)
                    print(data.decode())
                elif event & EPOLLOUT:
                    fdmap[fd].send(b'Receive')
                    #p.register(fd,EPOLLIN)

    def serve_forver(self):
        self.handle()




if __name__ == '__main__':
    port = 9999
    server = Server(port)
    server.serve_forver()