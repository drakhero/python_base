
# f = open('info.txt')
# s = f.readline()
# while s != '':
#     L = s.split(' ')
#     print("{} 今年 {}　岁,成绩是: {}".format(L[0],L[1],L[2]))
#     s = f.readline()
# f.close()

def read_info_txt():
    rl = []
    try:
        f = open("info.txt")
        L = f.readlines()
        for line in L:
            s = line.strip()
            name,age,score = s.split()
            age = int(age)
            score = int(score)
            rl.append({'name':name,'age':age,
                       'score':score})
        f.close()
        return rl
    except OSError:
        print("读取失败")

def print_info(L):
    for d in L:
        print(d['name'],'今年',d['age'],'岁,成绩是：',
                d['score'])

L = read_info_txt()

print_info(L)