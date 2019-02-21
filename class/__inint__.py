# class Car:
#     def __init__(self,c,b,m):
#         self.color = c
#         self.brand = b
#         self.model = m
#     def run(self,speed):
#         print(self.color,'的',self.brand,self.model,
#               '正在以',speed,'公里／小时的速度行驶')
#
# a4 = Car('黑色','奥迪','A4')
# a4.run(999)
#
# t1 = Car('蓝色','TESLA','Model S')
# t1.run(230)


# class list:
#     def __init__(self,iterable=None):
#         print("list的初始化方法被调用,iterable=",iterable)
# L = list()
# L = list("ABCD")



class Student:
    def __init__(self,name,age,score=None):
        self.name = name
        self.age = age
        self.score = score
    def set_score(self,score):
        if 0<=score<=100:
            self.score = score
    def show_info(self):
        print(self.name,self.age,self.score)
L = []
L.append(Student('小张',20,100))
L.append(Student('小李',18,95))
L.append(Student('小魏',8))
L[2].set_score(70)
for obj in L:
    obj.show_info()




















