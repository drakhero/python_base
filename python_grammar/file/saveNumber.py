# f = open('phone_book.txt','wt')
# while True:
#     name = input("姓名：")
#     if not name:
#         break
#     phone = input("号码：")
#     f.write(name+','+phone+'\n')
#
# f.close()

def input_info():
    L = []
    while True:
        name = input("姓名:")
        if not name:
            break
        number = input('号码：')
        t = (name,number)
        L.append(t)
    return L

def write_to_file(L):
    try:
        f = open("phone_book.txt",'w')
        for name, number in L:
            f.write(name+','+number+'\n')
        f.close()
    except OSError:
        print("写文件失败")

L = input_info()
write_to_file(L)