from threading import Thread,Lock
import time

lock1 = Lock()
lock2 = Lock()

def f1():
    lock1.acquire()
    print("线程１ 锁住了lock1")
    time.sleep(0.1)
    while True:
        result = lock2.acquire(timeout=1)
        if result:
            print("线程１　锁住了lock2")
            print("线程１ 你好")

            lock2.release()
            break
            #lock1.release()
        else:
            lock1.release()

def f2():
    lock2.acquire()
    print("线程2 锁住lock2")
    time.sleep(0.1)
    lock1.acquire()
    print("线程2　锁住了lock1")
    print("线程2 你好")

    lock1.release()
    lock2.release()

t1 = Thread(target=f1)
t2 = Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
