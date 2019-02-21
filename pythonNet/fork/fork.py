import os
from time import sleep
# print("********")
# a = 1
#
# pid = os.fork()
#
# if pid < 0:
#     print("创建进程失败")
# elif pid == 0:
#     print("这是新的进程")
#     print(a)
#     a = 1000
# else:
#     sleep(1)
#     print("这是原有进程")
#     print(a)
#
# print("演示结束")


pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("Child get pid:",os.getpid())
    print("Parent get pid",os.getppid())
else:
    sleep(2)
    print("parent get child pid",pid)
    print("parent get pid:",os.getpid())





