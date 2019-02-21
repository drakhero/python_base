#apply_async的返回值

from multiprocessing import Pool
import time

def f1(n):
    return n*n



if __name__ == "__main__":
    begin = time.time()
    pool = Pool(processes=6)

    rlist = []
    for i in range(1,7):
        robj = pool.apply_async(f1,args=(i,))
        rlist.append(robj)

    for r in rlist:
        print(r.get())

    pool.close()
    pool.join()
    end = time.time()
    print("执行时间:",end-begin)