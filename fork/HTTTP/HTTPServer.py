#coding = 'utf-8'
from socket import *
from threading import Thread
import sys,traceback

#httpserver类 封装具体的服务器功能
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        #创建套接字
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)


    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception:
                traceback.print_exc()
                continue
            #创建新的线程处理请求
            clientThread = Thread(target=self.handleRequest,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    #客户端请求函数
    def handleRequest(self,connfd):
        request = connfd.recv(4096)

        #解析请求内容
        requestHeaders = request.splitlines()
        print(connfd.getpeername(),":",requestHeaders[0])

        #获取具体请求内容
        getRequest = str(requestHeaders[0]).split()[1]

        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(getRequest,connfd)
        else:
            self.get_data(connfd,getRequest)
        connfd.close()

    #获取静态页面
    def get_html(self,getRequest,connfd):
        if getRequest == '/':
            filename = self.static_dir + "/index.html"
        else:
            filename = self.static_dir + getRequest
        try:
            f = open(filename)
        except Exception:
            #没有找到页面
            responseHeaders = "HTTP/1.1 404 NOT FOUND\r\n"
            responseHeaders += "\r\n"
            responseBody = "Sorry,not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = f.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    #获取数据
    def get_data(self,connfd,getRequest):
        urls = ['/time','/tedu','/python']

        if getRequest in urls:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            if getRequest == '/time':
                import time
                responseBody = time.ctime()
            elif getRequest == '/tedu':
                responseBody = "Welcome to tedu"
            elif getRequest == '/python':
                responseBody = "人生苦短我用Python"

        else:
            responseHeaders = "HTTP/1.1 404 NOT FOUND\r\n"
            responseHeaders += "\r\n"
            responseBody = "Sorry,not found the data"

        resonse = responseHeaders + responseBody
        connfd.send(resonse.encode())





if __name__ == "__main__":
    server_addr = ('0.0.0.0',8000)
    static_dir = './static'
    #生成对象
    http = HTTPServer(server_addr,static_dir)
    http.serve_forever()