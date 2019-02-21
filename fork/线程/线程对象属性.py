from threading import Thread,currentThread
import time

def f1():
    print("线程对象ｔ属性测试")
    time.sleep(1)
    print("%s 子线程执行完毕" % currentThread().getName())

if __name__ == "__main__":
    t = Thread(target=f1)
    #设置守护线程，一定要写在start()之前,不能和join()同时用
    #t.daemon = True
    #t.setDaemon(True)
    t.start()
    # print("线程名称",t.name)
    # print("线程名称",t.getName())
    t.setName("Tedu-1")
    # print("线程名称:",t.name)

    #t.join()
    print("主线程结束")