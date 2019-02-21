# try:
#     f = open("newfile.txt",'a') #第二个参数默认是：'rt'
#
#     f.write("hello")
#     f.write("world")
#     f.write('12\n')
#     f.writelines(['123','abc','ABC'])
#
#     f.close()
# except OSError:
#     print("创建失败")

f = open("mynote.txt")
for line in f:
    print(line)
f.close()
