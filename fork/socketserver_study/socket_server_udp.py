from socketserver import *

#创建服务器
class Server(ForkingUDPServer):
#class Server(ForkingMixIn,TCPServer):
    pass

class Handler(DatagramRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline(1024)
            print(self.client_address)
            if not data:
                break

            print(data.decode())
            self.wfile.write(b'Recvie')

if __name__ == "__main__":
    server_addr = ('0.0.0.0',9999)

    #创建服务器对象
    server = Server(server_addr,Handler)

    #启动服务器
    server.serve_forever()
