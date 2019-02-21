class Student:
    def __init__(self,s):
        self.__score = s

    @property
    def score(self):
        '''getter只用来获取数据'''
        return self.__score

    @score.setter
    def score(self,s):
        '''此方法用设置值加以限制以保证数据的准确性'''
        print("setter被调用")
        if 0 <= s <= 100:
            self.__score = s

    # def setScore(self,s):
    #     '''只用来设置数据'''
    #     if 0<=s<=100:
    #         self.__score = s

    # def getScore(self):
    #     '''只用来获取数据'''
    #     return self.__score

s = Student(50)
#print(s.__score) #出错
#s.setScore(100)
s.score = 100
score = s.score
print(score)