class Student:
    L = []

    def __init__(self,n,a,s=0):
        self.name = n
        self.age = a
        self.score = s

    @classmethod
    def add_student(cls):
        cls.L.append(Student('小张', 20, 100))
        cls.L.append(Student('小李', 18, 95))
        cls.L.append(Student('小魏', 16, 90))

    @classmethod
    def del_student(cls):
        del cls.L[0]

    @classmethod
    def get_student_count(cls):
        return len(cls.L)

    @classmethod
    def get_avg_score(cls):
        return sum(map(lambda obj:obj.score,cls.L))/len(cls.L)

    @classmethod
    def get_avg_age(cls):
        return sum(map(lambda obj:obj.age,cls.L))/len(cls.L)


Student.add_student()
print("学生个数：",Student.get_student_count())
print("学生平均成绩：",Student.get_avg_score())
print("学生平均年龄：",Student.get_avg_age())
Student.del_student()
print("学生个数：",Student.get_student_count())
print("学生平均成绩：",Student.get_avg_score())
print("学生平均年龄：",Student.get_avg_age())