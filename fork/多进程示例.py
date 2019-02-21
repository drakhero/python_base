from multiprocessing import Process
import os,time

#事件1
def sing():
    print("singing start, my father is %d" % os.getppid())
    time.sleep(1)

#事件2
def dance():
    print("dancing start, my father is %d" % os.getppid())
    time.sleep(1)

#时间3
def eat():
    print("eating start, my father is %d" % os.getppid())
    time.sleep(1)
start = time.time()

#创建进程对象
likes = [sing,dance,eat]
processes = []
for like in likes:
    p = Process(target=like)
    p.start()
    processes.append(p)

#回收进程
#当sing进程没结束，dance和eat已经结束，此时操作系统会记录dance和eat的完成状态，等sing结束后直接回收dance和eat

for ps in processes:
    ps.join()

# p1 = Process(target=sing)
# p2 = Process(target=dance)
# p3 = Process(target=eat)
# #启动进程
# p1.start()
# p2.start()
# p3.start()

#回收进程
# p1.join()
# p2.join()
# p3.join()

end = time.time()
print("运行时间:%.2f" % (end-start))