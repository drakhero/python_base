
try:
    f = open('mynote.txt',mode='rt')
    if f:
        print("success")
    s = f.readline()
    print(s)
    s = f.readline()
    print(s)
    s = f.readline()
    print(s)
    f.close()
    if  f :
        print("文件已关闭")
except OSError:
    print("文件打开失败")