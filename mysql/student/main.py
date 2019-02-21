from stu_class import Student

import oper

while True:
    print("q--退出")
    print("1--添加")
    print("2--删除")
    s = input("输入选项: ")

    if s == 'q':
        break

    if s == '1':
       oper.stu_add()

    if s == '2':
        oper.stu_delete()
