def get_age():
    try:
        age = int(input())
        if age > 140 or age < 1:
            raise ValueError("您的输入不在1~140")
        return age
    except:
        raise
try:
    age = get_age()
    print("用户输入的年龄是：",age)
except ValueError as err:
    print("用户输入的不是1~140的整数，获取年龄失败！",err)