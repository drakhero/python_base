import time

# while True:
#     t = time.localtime()
#     print("{}:{}:{}".format(*t[3:6]),end='\r')
#     #print("%02d:%02d:%02d" % t[3:6], end = '\r')
#     time.sleep(1)

h = int(input())
m = int(input())


while True:
    t = time.localtime()
    if t[3:5] == (h,m):
        print("时间到")
        break
    time.sleep(1)
