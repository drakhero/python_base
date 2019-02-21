
#算术运算符重载的方法
class MyNumber:
    def __init__(self,v):
        self.data = v

    def __add__(self, other):
        return MyNumber(self.data + other.data)

    def __sub__(self, other):
        return MyNumber(self.data - other.data)

    def __repr__(self):
        return "MyNumber(%d)" % self.data

n1 = MyNumber(100)
n2 = MyNumber(200)
n3 = n1 + n2 #等同于　n3 = n1.__add__(n2)
# print(n3)
# n4 = n3 - n2
# print(n4)

#****************************


class MyList:
    def __init__(self, iterable=()):
        self.__data = list(iterable)

    def __add__(self, other):
        return MyList(self.__data+other.__data)

    def __mul__(self, other):
        return MyList(self.__data*other)

    def __rmul__(self, other):
        return MyList(self.__data*other)

    def __iadd__(self, other):
        print("iadd")
        self.__data += other.__data
        return self

    def __neg__(self):
        return MyList((-x for x in self.__data))

    def __lt__(self, other):
        return self.__data < other.__data


    def __contains__(self, item):
        return  item in self.__data


    def __getitem__(self, item):
        print('item的值是：', item)
        if type(item) is int :
            print("用户正在用索引取值")
        elif type(item) is slice:
            print("用户正在用切片取值")
            print("切片的起点是：",item.start)
            print("切片的终点是:",item.stop)
            print("切片的步长是：",item.step)
        elif type(item) is str:
            print("用户正在用字符串进行索引操作")
            #raise KeyError
            return  "你想字符串做什么？"

        return self.__data[item]


    def __setitem__(self, key, value):
        self.__data[key] = value

    def __delitem__(self, key):
        del self.__data[key]


    def __repr__(self):
        return "MyList(%s)" % self.__data



L1 = MyList([1,2,3])
L2 = MyList([4,5,6])
#L3 = L1 + L2
# print(L3)
# L4 = L2 + L1
# print(L4)
# L5 = L1*3
# print(L5)
#
# L6 = 3*L2
# print(L6)

#********************
# print(id(L1))
# L1 += L2
# print(id(L1))
# L2 *= 3
# print(L2)

#********************

#一元运算符重载

L1 = MyList([1,-2,3,-4,5])
L2 = -L1
# print(L2)
#
#print(L2 < L1)


#*******************
#in / not in

L1 = MyList([1,-2,3,-4,5])

if 2 in L1:
    print("2在L1内")
else:
    print("2不在L1内")

if 4 not in L1:
    print("4不在L1内")
else:
    print("4在L2内")

#********************

L1 = MyList([1,-2,3,-4])
x = L1[3]
print(x)
L1[0] = 4
print(L1)
del L1[1]
print(L1)
print(L1[::2])
print(L1[slice(None,None,2)])#切片对象
print(L1['aa'])




