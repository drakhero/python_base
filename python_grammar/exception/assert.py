def get_score():
    s = int(input("请输入学生成绩(0~100):"))
    assert 0<= s <= 100, '成绩超出范围'
    return s

try:
    score = get_score()
    print("学生成绩为：",score)
except ValueError:
    print("用户的输入不能转为整数")
except AssertionError:
    print("用户输入的整数不在0~100之间")