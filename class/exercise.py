# class Human:
#     total_count = 0
#     pass
#
# print(Human.total_count)
# h1 = Human()
# print(h1.total_count)
# h1.total_count = 10000
# print(h1.total_count)
# print(Human.total_count)
#
# h1.__class__.total_count = 5
# print(Human.total_count)


# class Human:
#     total_count = 0
#
#     def __init__(self,n):
#         self.name = n
#         self.__class__.total_count += 1
#         print(n,'对象创建')
#
#     def __del__(self):
#         print(self.name,'对象被销毁')
#         self.__class__.total_count -= 1
#
# L = []
# L.append(Human('张飞'))
# L.append(Human('关羽'))
# print("当前人物个数是：",Human.total_count)
# del L[1]
# print("当前人物个数是：",Human.total_count)


class Student:
    __slots__ = ['name','age','score']
    count = 0
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
        self.__class__.count += 1
    @staticmethod
    def getCount():
        return Student.count


L = []
def add_student(L):
    L.append(Student('小张',20,100))
    L.append(Student('小李',18,95))
    L.append(Student('小魏',16,90))
print(Student.count)
aveS = 0
for obj in L:
    aveS += int(obj.score)
print(aveS/Student.count)

aveA = 0
for obj in L:
    aveA += int(obj.age)
print(aveA/Student.count)















