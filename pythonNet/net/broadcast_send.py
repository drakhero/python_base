from socket import *
from time import sleep

#设置目标地址
#dest = ('10.8.31.255',9999)
dest = "<broadcast>"

s = socket(AF_INET,SOCK_DGRAM)

#设置能够发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("初庭徽已被管理员禁言".encode(),(dest,9999))
s.close()