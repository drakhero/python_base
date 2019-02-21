#用finally保证关闭文件
try:
    f = open("finally.py")
    try:
        for l in f:
            x = int('aaa')
            print(l)
    finally:
        f.close()


except OSError:
    print("打开失败")

#用with语句保证关闭文件
try:
    with open("finally.txt") as f:
        for l in f:
            x = int('aaa')
            print(l)
except OSError:
    print("打开失败")
