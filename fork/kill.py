import os
import signal

#向5226发送信号
os.kill(5226,signal.SIGKILL)