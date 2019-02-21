class A:
    def __init__(self):
        self.__p1 = 100#私有
        self.__p2__ = 200 #不是私有属性
    def show_info(self):
        print(self.__p1)#此对象的实例方法可以访问和修改私有属性
        self.__privite()#调用私有方法

    def __privite(self):
        print("I am a privite way")

a = A()
a.show_info()

# print(a.__p1)
# print(a.__p2__)