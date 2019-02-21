

#cpu密集型
def CPU(x,y):
    z = 0
    while z < 7000000:
        x += 1
        y += 1
        z += 1

#I/O密集型
def write():
    f = open("test.txt",'a')
    for i in range(150000):
        f.write("hello world\n")
    f.close()

def read():
    f = open("test.txt")
    lines = f.readlines()
    f.close()

def IO():
    write()
    read()


from multiprocessing import Process
from threading import Thread
import time

#多线程处理cpu密集型
# begin = time.time()
# threads = []
# for i in range(10):
#     t = Thread(target=CPU,args=(1,1))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# end = time.time()
# print("多线程处理CPU密集型: %.2f" % (end-begin))
#
# #多进程处理cpu密集型
# begin = time.time()
# processes = []
# for i in range(10):
#     p = Process(target=CPU,args=(1,1))
#     processes.append(p)
#     p.start()
#
# for p in processes:
#     p.join()
#
# end = time.time()
# print("多进程处理CPU密集型: %.2f" % (end-begin))


#多线程执行I/O操作密集型
begin = time.time()
threads = []
for i in range(10):
    t = Thread(target=IO)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()
print("多线程处理IO密集型: %.2f" % (end-begin))

#多进程执行I/O操作密集型
# begin = time.time()
# processes = []
# for i in range(10):
#     p = Process(target=IO)
#     processes.append(p)
#     p.start()
#
# for p in processes:
#     p.join()
#
# end = time.time()
# print("多进程处理IO密集型: %.2f" % (end-begin))

























