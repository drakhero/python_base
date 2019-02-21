class Student():
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    @property
    def getId(self):
        return self.id

    @property
    def getName(self):
        return self.name

    @getName.setter
    def setName(self, name):
        self.name = name

    @property
    def getAge(self):
        return self.age

    @getAge.setter
    def setAge(self,age):
        self.age = age

# s = Student(1,"tom",34)
# s.setId = 2
# print(s.getId,s.getName,s.getAge)
