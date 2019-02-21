import copy

def write_info(L):
    try:
        file = input("请输入您要保存的文件名：")
        f = open(file,'a')
        for student in L:
            if student != L[len(L)-1]:
                f.write(student+",")
            else:
                f.write(student)
    except OSError:
        print("文件写入失败")
    finally:
        f.close()

def input_info():
    L  = []
    while True:
        s = input("请输入学生姓名: ")
        L.append(s)
        sign = input("是否继续？y是n否").lower()
        if sign != 'y':
            break
    write_info(L)
    return L

def load_info():
    file = input("请输入文件路径：")
    try:
        f = open(file)
        s = f.read()
        L = s.strip().split(',')
        print(s)

    except OSError:
        print("读取文件失败")
    finally:
        f.close()
    return L

def show_menu():
    print("1) 新建名单")
    print("2) 点名")

import random

def calling(L):
    roll = copy.deepcopy(L)
    if not roll:
        print("没有加载名单")
        sign = input("是否导入名单? Y/y导入名单,n/N退出并显示菜单: ").lower()
        if sign == 'n':
            show_menu()
            return
        if sign == 'y':
            roll = load_info()

    if roll:
        while True:
            num = int(input("输入要随机点取的学生个数："))
            if num>0 and num <= len(roll):
                break
            else:
                print("非法输入,请重新输入")
        stu_call = random.sample(roll,num)
        print(roll)
        print(stu_call)
        for student in stu_call:
            input("按下回车点名")
            print(student)


def main():
    info = []

    while True:
        show_menu()
        key = input("输入：")
        if key == '1':
            info = input_info()
        elif key == '2':
            calling(info)
        elif key == 'q':
            break
        else:
            print("输入错误，请重新输入")



main()







