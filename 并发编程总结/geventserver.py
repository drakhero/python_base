import gevent
from gevent import monkey
import traceback

monkey.patch_all()

from socket import *

class Server(object):
    def __init__(self,port):
        self.port = port
        self.createSocket()

    def createSocket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(('',self.port))
        self.sockfd.listen(5)

    def handle(self,connfd):
        while True:
            try:
                data = connfd.recv(1024)
            except Exception:
                break
            if not data:
                print("客户端退出")
                break
            print(data.decode())
            connfd.send(b'Receive')
        connfd.close()

    def serve_forever(self):
        while True:
            try:
                connfd,addr = self.sockfd.accept()
                print("Connect from",addr)
            except InterruptedError:
                sys.exit("服务器退出")
            except Exception:
                traceback.print_exc()
                sys.exit(0)

            gevent.spawn(self.handle,connfd)



if __name__ == "__main__":
    port = 9999
    server = Server(port)
    server.serve_forever()
