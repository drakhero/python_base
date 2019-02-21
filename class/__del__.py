class Car:
    def __init__(self,info):
        self.info = info
        print("汽车对象",info,'被创建')
    def __del__(self):
        print("汽车对象",self.info,'被销毁')

c1 = Car("BYD E6")
del c1
input("请输入回车键继续执行程序：")
print("程序退出")