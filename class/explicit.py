
#显示调用父类方法
class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        print("Human类的初始化方法被调用...")

    def infos(self):
        print("姓名：",self.name)
        print("年龄:", self.age)

class Student(Human):
    def __init__(self,n,a,s=0):
        super(Student,self).__init__(n,a)
        self.score = s

    def infos(self):
        super().infos() #显示调用父类
        print('成绩',self.score)

s1 = Student('张飞', 15,80)
s1.infos()







