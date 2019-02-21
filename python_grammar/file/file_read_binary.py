#用二进制方式读取文件内容

try:
    fr = open('mybinary.bin','rb')
    b = fr.read()
    print(b)
    fr.close()

except OSError:
    print("打开二进制文件失败")