from multiprocessing import Process
import time
#定义变量
name = "赵敏"

#定义函数
def f1():
    global name
    print("子进程name=%s" % name)
    name = "周芷若"
    print("子进程name=%s" % name)
    time.sleep(5)
#创建进程对象
p = Process(target=f1)
p.start()

#父进程
print("父进程name=%s" % name)

#回收子进程,阻塞函数
p.join()

#父进程
print("父进程name=%s" % name)
while True:
    pass