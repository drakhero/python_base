from socket import  *

# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

while True:
    c,addr = s.accept()
    print("Connect from",addr)
    data = c.recv(4096)
    print("*******************")
    print(data)
    print("*******************")

    data = '''HTTP/1.1 200 OK
    Content-Encoding: gzip
    Content-Type: text/html

    <h1>welcome to here</h1>
    '''
    print(data.encode())


    # data = '''HTTP/1.1 200 OK
    # Content-Encoding: gzip
    # Content-Type: text/html

    # <h1>Welcome to here</h1>
    # '''
    # print(data.encode())
    c.send(data.encode())
    c.close()

s.close()