from multiprocessing import Pool
import time

def automan(n):
    print("奥特曼进入进程池",n)
    time.sleep(1)



pool = Pool(processes=100)

for i in range(1,10000):
    pool.apply_async(func=automan,args=(i,))

pool.close()


pool.join()