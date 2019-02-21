class A():
    def work(self):
        print("A.work()被调用")

class B(A):
    def work(self):
        print("B.work被调用")

    def super_work(self):
        self.work()
        super(B,self).work()
        super(self.__class__,self).work()
        super().work() #必须在方法内调用

b = B()
#b.work()
#super(B,b).work()
b.super_work()