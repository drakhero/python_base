class MyList(list):
    def insert_head(self,x):
        #self[0:0] = [x]
        #self.insert(0,x)
        self = [3,3]
        print(self)

myl = MyList(range(3,6))
print(myl)
myl.insert_head(2)
print(myl)
