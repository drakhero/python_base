import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("create process failed")

elif pid == 0:
    sleep(3)
    print("Child process exit",os.getpid())
    os._exit(4)
else:
    pid,status = os.wait()
    print(pid,status)
    print(os.WEXITSTATUS(status))
