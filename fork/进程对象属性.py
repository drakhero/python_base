from multiprocessing import Process
import time

#写函数，每隔一秒打印当前时间，打印n次
def timing(n):
    for i in range(n):
        print(time.ctime())
        time.sleep(1)


#创建进程
p = Process(target=timing,args=(10,),name="计时器")
# print("name:",p.name)
# print("PID:",p.pid)
# print("alive:",p.is_alive())

p.daemon = True #设置为守护进程，主进程结束，子进程跟着结束

#启动进程
p.start()
print("name:",p.name)
print("PID:",p.pid)
print("alive:",p.is_alive())
#回收进程
#p.join()






