from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,n):
        super().__init__()
        self.n = n

    def fun1(self):
        for i in range(self.n):
            print("子进程在做事")
            time.sleep(1)
    #重写run方法,父类中对此方法做了自动化处理，如果换了方法就找不到了
    def run(self):
        self.fun1()


if __name__ == '__main__':
    start = time.time()

    p = MyProcess(3)
    p.start()
    p.join()
    print("我是父进程")
    end = time.time()
    print("执行时间 %f" % (end-start))