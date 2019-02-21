class MyNumber:
    def __init__(self,val):
        self.data = val

    def __repr__(self):
        return  "MyNumber(%d)" % self.data

    def __str__(self):
        return "自定义数字：%d" % self.data

n1 = MyNumber(100)

print(n1)