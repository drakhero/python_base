from multiprocessing import Process
import time,os

#事件1
def somke(name,number):
    print("抽烟进程：%d 启动, %s 抽了 %d 根烟" % (os.getpid(),name,number))

def drink(name):
    print("drink %s drinking" % name)

def hair(name):
    print("hair %s hairing" % name)


start = time.time()

p1 = Process(target=somke,args=("于谦",5))
p2 = Process(target=drink,args=("魏叔叔",))
p3 = Process(target=hair,args=("超哥哥",))

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

end = time.time()
print("执行时间： %.2f" % (end-start))