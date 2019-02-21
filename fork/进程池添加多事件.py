from multiprocessing import Pool

def automan(n):
    print("奥特曼 %d 进入进程池" % n)

def guaishou(n):
    print("怪兽 %d 开始战斗" % n)

pool = Pool(processes=4)

for i in range(1,7):
    pool.apply_async(func=automan,args=(i,))
    pool.apply_async(func=guaishou,args=(i,))



pool.close()
pool.join()