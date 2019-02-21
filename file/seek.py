# f = open('mynote.txt','rb')
# b = f.read(3)
#
# print(b)
# pos = f.tell()
# print("当前的读写位置: ",pos)
# b2 = f.read(1)
# print(b2)
# print("再读一个字节后的读写位置是：　",f.tell())
# f.close()


f = open('mynote.txt','rb')
b = f.read(3)
print(b)

f.seek(5,0) # 移动读写位置
b = f.read(1)
print(b)
f.close()





