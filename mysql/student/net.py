from socket import *

sockdf = socket()
sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
socket.bind(("0.0.0.0",8888))
socket.listen(5)