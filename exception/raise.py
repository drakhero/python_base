def make_except():
    print("开始")
    #raise ValueError
    e = ValueError("这是故意制作的一个错误")
    raise e
    print("结束")

def get_except():
    try:
        make_except()
    except ValueError as err:
        print("make_except发出了ValueError")
        print("错误值:", err)
        raise
try:
    get_except()
except ValueError as err:
    print("get_except内部发生错误")

print("程序结束")