# L= []
# while True:
#     s = input()
#     if s == '':
#         break
#     s+='\n'
#     L.append(s)
#
# f = open("input.txt",'wt')
# for x in L:
#     f.write(x)
# f.close()
#
# f = open("input.txt")
# Lin = f.readlines()
# for x in Lin:
#     print(x)



def read_from_file(filename='input.txt'):
    L = []
    try:
        fr = open(filename,'rt')
        for line in fr:
            s = line.rstrip()
            L.append(s)
        fr.close()
        print("读取文件成功")
    except OSError:
        print("打开读取文件失败!!!")
    return L

def print_text(lst):
    for line_number,s in enumerate(lst,1):
        print(line_number,":",s)

if __name__ == '__main__':
    print_text(read_from_file())





















