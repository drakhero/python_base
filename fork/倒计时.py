from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,n):
        self.n = n
        super().__init__()

    def timeResever(self):
        for i in range(self.n,0,-1):
            print(i)
            time.sleep(1)

    def run(self):
        self.timeResever()
        print("结束")

if __name__ == '__main__':
    p = MyProcess(5)
    p.start()
    p.join()