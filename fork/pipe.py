from multiprocessing import Process,Pipe
import os,time

fd1,fd2 = Pipe()

def fun(name):
    time.sleep(3)
    fd1.send("hello "+str(name))

jobs = []
for i in range(5):
    p = Process(target=fun,args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data  = fd2.recv()
    print(data)

for i in jobs:
    i.join()