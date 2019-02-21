class Student:
    def __init__(self,n,s,a):
        self.name = n
        self.score = s
        self.age = a

    def get_info(self):
        return self.name,self.score,self.age

    @property
    def get_name(self):
        return self.name

    @property
    def get_score(self):
        return self.score

    @property
    def get_age(self):
        return self.age

    def set_score(self,s):
        if 0 <= s <= 100:
            self.score = s
