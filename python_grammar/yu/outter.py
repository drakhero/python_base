# def out():
#     x = 1
#     def inner():
#         print(x)
#     inner()
# out()

#******************

#函数式编程
def add(x,y):
    return x+y
def sub(x,y):
    return x-y

def apply(fn,x,y):
    return fn(x,y)

apply(add,20,10)

#*****************

def outer(fn):
    def inner():
        print("before fn")
        result = fn()
        print(result+1)
    return inner
def foo():
    return 10

decorated = outer(foo)
decorated()

#***********************
def prive_check(fn):
    def notice(name,x):
        print('验证成功')
        fn(name,x)
    return notice

@prive_check
def save_money(name,x):
    print("{}存钱{}元".format(name,x))
#save_money = prive_check(save_money)
#save_money('小张',200)
save_money('小张',200)
