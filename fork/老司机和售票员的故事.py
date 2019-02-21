from multiprocessing import Process
from signal import *
from time import sleep
import os,sys



def hander_diver(sig, frame):
    if sig == SIGUSR1:
        print("老司机开车了")
    elif sig == SIGUSR2:
        print("车速优点快，系好安全带")
    elif sig == SIGTSTP:
        os.kill(conductor.pid,SIGUSR1)



def hander_conductor(sig, frame):
    if sig == SIGINT:
        os.kill(os.getppid(), SIGUSR1)

    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)

    elif sig == SIGUSR1:
        print("到站了，请下车")
        sys.exit(0)

def cdor():
    signal(SIGINT,hander_conductor)
    signal(SIGQUIT,hander_conductor)
    signal(SIGUSR1,hander_conductor)
    signal(SIGTSTP,SIG_IGN)
    while True:
        sleep(2)
        print("python带你去远方")

conductor = Process(target=cdor)
conductor.start()

signal(SIGUSR1,hander_diver)
signal(SIGUSR2,hander_diver)
signal(SIGTSTP,hander_diver)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)

conductor.join()