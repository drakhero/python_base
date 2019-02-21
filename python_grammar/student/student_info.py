from python_grammar import student


def input_student(L):
    while True:
        name = input("请输入姓名: ")
        if name == '':
            break
        try:
            score = int(input("请输入成绩: "))
            age = int(input("请输入年龄: "))
            L.append(student.Student(name, score, age))
        except ValueError:
            print("输入错误,请输入回车重新输入")
            input()
            continue



def output_student(L):
    print("+--------------+----------+----------+")
    print("|    姓名      |   年龄　 |　　成绩　|")
    print('+--------------+----------+----------+')
    for student in L:
        print('|',end='')
        print(student.get_name.center(13)+' |',end='')
        print(str(student.get_age).center(10) + '|',end='')
        print(str(student.get_score).center(10) + '|')
        print('+--------------+----------+----------+')



def delt(L):
    s = input("请输入您要删除的学生姓名：　")
    for i in range(0,len(L)):
        if s == L[i].get_name:
            del L[i]
            print("删除成功")
            break
    else:
        print("删除失败")

def update(L):
    s = input("请输入您要修改的成绩的学生姓名: ")
    score = int(input("请输入该生的新成绩：　"))
    for student in L:
        if s == student.get_name:
            student.set_score(score)
            print(student.get_name,student.get_score)
            print("修改成功")
            break
    else:
        print("这个学生不存在")


def scoreSort(infos):
    L = sorted(infos,key=lambda s:s.get_score)
    output_student(L)

def scoreSortReverse(infos):
    L = sorted(infos, key=lambda s: s.get_score,reverse=True)
    output_student(L)

def ageSort(infos):
    L = sorted(infos, key=lambda s: s.get_age)
    output_student(L)

def ageSortReverse(infos):
    L = sorted(infos, key=lambda s: s.get_age,reverse=True)
    output_student(L)


def readInfo():
    info = []
    try:
        try:
            f = open('info.txt','rt')
            for s in f:
                name,score,age = str(s).strip().split(',')
                name = str(name)
                score = int(score)
                age = int(age)
                info.append(student.Student(name, score, age))
        finally:
            f.close()
    except OSError:
        print('读文件失败')
    return info


def writeInfo(L):
    try:
        try:
            f = open('info.txt','at')
            for s in L:
                name, score, age = s.get_name, s.get_score, s.get_age
                f.writelines('\n' + name + ',' + str(score)  + ',' + str(age))
        finally:
            f.close()
    except OSError:
        print("写入文件失败")










