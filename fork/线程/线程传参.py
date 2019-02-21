from threading import Thread
import time

#线程函数
def f1(name,seconds):
    print("%s 线程开始执行" % name)
    time.sleep(seconds)
    print("%s 线程执行完毕，时间 %d 秒" % (name,seconds))


if __name__ == "__main__":
    #创建空列表存放线程对象
    threads = []
    for i in range(3):
        #t = Thread(target=f1,args=(i+1,2))
        t = Thread(target=f1, kwargs={'name':"Tedu-%d"%i,'seconds':2})
        threads.append(t)
        t.start()

    for m in threads:
        m.join()
