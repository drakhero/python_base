from multiprocessing import Process

def fun1():
    name = input("请输入姓名: ")

#创建进程对象，此时还没有创建进程
p = Process(target=fun1)

#创建进程并执行关联函数
p.start()

print("我是父进程")