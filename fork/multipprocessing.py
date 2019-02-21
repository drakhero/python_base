from multiprocessing import Process
import time
#事件1
def fun1():
    print("子进程做事件1")

#创建1个进程
p = Process(target=fun1)
#进程启动,执行fun1函数中的代码
p.start()

time.sleep(1)
#父进程
print('父进程在做事')




