import threading
from time import sleep
import os

#线程函数
def music():
    for i in range(2):
        sleep(2)
        print("播放葫芦娃",os.getpid())
        global n
        n = 1000
        print("分支线程n=",n)

if __name__ == '__main__':
    #创建线程对象
    t = threading.Thread(target=music)
    t.start()
    t.join()
    #主线程
    for i in range(2):
        sleep(3)
        print("灌篮高手",os.getpid())
    print("主线程:n=",n)
