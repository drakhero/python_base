from threading import Thread,Lock

m = 0
n = 0

#线程函数
def f1():
    while True:
        lock.acquire()
        if m != n:
            print("m=",m,"n=",n)
        lock.release()

if __name__ == "__main__":
    lock = Lock()
    t = Thread(target=f1)
    t.start()

    while True:
        with lock:
            m += 1
            n += 1

    t.join()