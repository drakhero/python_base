def get_score():
    try:
        s = float(input("请输入成绩："))
    except ValueError:
        print("类型错误")
    if 0 <= s <=100:
        return s
    else:
        return 0


score = get_score()
print("学生成绩是：",score)