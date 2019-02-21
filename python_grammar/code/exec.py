# s = '''
# x=100
# y=200
# print('x+y=',x+y)
# del x,y
# '''
# exec(s)

def my():
    local_dict = {}

    while True:
        s = input("请输入程序：>>>")
        if s == 'quit()':
            break
        exec(s,globals=globals())
    print(local_dict)


my()