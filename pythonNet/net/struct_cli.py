#struct 格式转换示例

from socket import *
import struct

address = ("127.0.0.1",9999)

client = socket(AF_INET,SOCK_DGRAM)

while True:
    id = int(input("id:"))
    name = input("name:")
    n = len(name.encode())
    height = float(input("height:"))

    fmt = "i%dsf" % n   # i4sf
    print(n)
    #按照格式转换字节序列
    data = struct.pack(fmt,id,name.encode(),height)

    client.sendto(fmt.encode(),address)

    #发送数据
    client.sendto(data,address)

client.close()
