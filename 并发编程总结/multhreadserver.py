from threading import Thread
from socket import *
import traceback
import sys

class Server(object):
    def __init__(self,port):
        self.port = port
        self.createSocket()

    def createSocket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(("",self.port))
        self.sockfd.listen(5)

    def handle(self,connfd):
        while True:
            data = connfd.recv(1024)
            if not data:
                print("客户端退出")
                break
            print(data.decode())
            connfd.send(b"Receive")
        connfd.close()

    def serve_forever(self):
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception:
                traceback.print_exc()
                self.sockfd.close()
                sys.exit(0)
            print("Connect from",addr)
            t = Thread(target=self.handle,args=(connfd,))

            t.setDaemon(True)
            t.start()

if __name__ == "__main__":
    port = 9999
    server = Server(port)
    server.serve_forever()