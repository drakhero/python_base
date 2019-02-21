import show_menu
from student_info import *

def main():
    infos = []
    while True:
        show_menu.show_menu()
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
        elif s == '9':
            infos = readInfo()
        elif s == '10':
            writeInfo(infos)
        else:
            print("输入错误,请重新输入")

main()