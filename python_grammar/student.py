 #    {'name':'tarena','age':'11','score':'88'},{'name':'home','age':'22','score':'80'}
def input_student(L):
    while True:
        d = {}
        x = input("请输入姓名: ")
        if x == '':
            break
        d['name'] = x
        x = input("请输入成绩: ")
        d['score'] = x
        x = input("请输入年龄: ")
        d['age'] = x
        L.append(d)

def output_student(L):
    print("+--------------+----------+----------+")
    print("|     姓名      |   年龄　　｜　　成绩　　|")
    print('+--------------+----------+----------+')
    for dic in L:
        print('|',end='')
        print(dic['name'].center(13)+' |',end='')
        print(dic['age'].center(10) + '|',end='')
        print(dic['score'].center(10) + '|')
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
    score = input("请输入该生的新成绩：　")
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

def show_menu():
    print('+---------------------------+')
    print("| 1)添加学生信息".ljust(24) + '|')
    print("| 2)显示学生信息".ljust(24) + '|')
    print("| 3)删除学生信息".ljust(24) + '|')
    print("| 4)修改学生成绩".ljust(24) + '|')
    print("| 5)按学生成绩高~低显示学生信息".ljust(20) + '|')
    print("| 6)按学生成绩低~高显示学生信息".ljust(20) + '|')
    print("| 7)按学生年龄高~低显示学生信息".ljust(20) + '|')
    print("| 8)按学生年龄低~高显示学生信息".ljust(20) + '|')


    print("| q)退出　　　　".ljust(24) + '|')
    print("+---------------------------+")

def main():
    infos = []
    while True:
        show_menu()
        s = input()
        if s == 'q':
            break
        elif s == '1':
            input_student(infos)
        elif s == '2':
            output_student(infos)
        elif s == '3':
            delt(infos)
        elif s == '4':
            update(infos)
        elif s == '5':
            scoreSortReverse(infos)
        elif s == '6':
            scoreSort(infos)
        elif s == '7':
            ageSortReverse(infos)
        elif s == '8':
            ageSort(infos)
        else:
            print("输入错误,请重新输入")



main()


































