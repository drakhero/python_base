class Human:
    __slots__ = ['name','age'] #防止因写错属性名而引发错误

    def __init__(self,n,a):
        self.name = n
        self.age = a

    def info(self):
        print(self.name,'今年',self.age,'岁')

h1 = Human('小张',8)
h1.info()
h1.age = 9
h1.info()