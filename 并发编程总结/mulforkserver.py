from multiprocessing import Process
from socket import *
import sys
import traceback


class Server(object):
    def __init__(self,port):
        self.port = port
        self.createSocket()

    def createSocket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(('',self.port))
        self.sockfd.listen(5)

    def handle(self):
        self.sockfd.close()
        while True:
            data = self.connfd.recv(1024)
            if not data:
                self.connfd.close()
                sys.exit("客户端退出")
            print(data.decode())
            self.connfd.send(b"Receive")
        self.connfd.close()

    def serve_forver(self):
        while True:
            try:
                self.connfd,self.addr = self.sockfd.accept()
                print("Connect from",self.addr)
            except KeyboardInterrupt:
                sys.exit("服务器退出")
            except Exception:
                self.sockfd.close()
                traceback.print_exc()
                sys.exit(0)
            p = Process(target=self.handle)
            p.daemon = True
            p.start()
            self.connfd.close()



if __name__ == "__main__":
    port = 7777
    server = Server(port)
    server.serve_forver()