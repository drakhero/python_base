#二进制文件写操作

try:
    fbw = open("mybinary.bin",'wb')
    s = '你好'
    b = s.encode('utf-8')
    fbw.write(b)
    ba = bytearray(range(256))
    fbw.write(ba)
    fbw.close()
    print("文件写入成功")


except OSError:
    print("Failed")