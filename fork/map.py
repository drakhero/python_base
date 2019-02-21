from multiprocessing import Pool
import time

def f1(n):
    return n*n

pool = Pool(processes=6)

rlist = pool.map(f1,range(10000000))
pool.close()
pool.join()

print(rlist)