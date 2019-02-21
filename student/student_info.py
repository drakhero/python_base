
def input_student(L):
    while True:
        d = {}
        x = input("请输入姓名: ")
        if x == '':
            break
        d['name'] = x
        try:
            x = int(input("请输入成绩: "))
            d['score'] = x
            x = int(input("请输入年龄: "))
            d['age'] = x
            L.append(d)
        except ValueError:
            print("输入错误,请输入回车重新输入")
            input()
            continue

def output_student(L):
    print("+--------------+----------+----------+")
    print("|     姓名      |   年龄　　｜　　成绩　　|")
    print('+--------------+----------+----------+')
    for dic in L:
        print('|',end='')
        print(dic['name'].center(13)+' |',end='')
        print(str(dic['age']).center(10) + '|',end='')
        print(str(dic['score']).center(10) + '|')
        print('+--------------+----------+----------+')



def delt(L):
    s = input("请输入您要删除的学生姓名：　")
    for i in range(0,len(L)):
        if s == L[i]['name']:
            del L[i]
            print("删除成功")
            break
    else:
        print("删除失败")

def update(L):
    s = input("请输入您要修改的成绩的学生姓名: ")
    score = int(input("请输入该生的新成绩：　"))
    for i in range(0,len(L)):
        if s == L[i]['name']:
            L[i]['score'] = score
            print("修改成功")
            break
    else:
        print("这个学生不存在")

def scoreSort(infos):
    L = sorted(infos,key=lambda i:i['score'])
    output_student(L)

def scoreSortReverse(infos):
    L = sorted(infos, key=lambda i: i['score'],reverse=True)
    output_student(L)

def ageSort(infos):
    L = sorted(infos, key=lambda i: i['age'])
    output_student(L)

def ageSortReverse(infos):
    L = sorted(infos, key=lambda i: i['age'],reverse=True)
    output_student(L)


def readInfo():
    info = []
    try:
        try:
            f = open('info.txt','rt')
            for student in f:
                d = {}
                name,score,age = str(student).strip().split(',')
                d['name'] = str(name)
                d['score'] = str(score)
                d['age'] = str(age)
                info.append(d)
        finally:
            f.close()
    except OSError:
        print('读文件失败')
    return info


def writeInfo(L):
    try:
        try:
            f = open('info.txt','at')
            for d in L:
                name, score, age = d['name'], d['score'], d['age']
                f.writelines('\n' + name + ',' + str(score)  + ',' + str(age))
        finally:
            f.close()
    except OSError:
        print("写入文件失败")










