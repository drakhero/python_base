import os,sys

#os._exit(0)

try:
    sys.exit("退出")
except SystemExit as e:
    print("退出",e)

print("process exit")


