
class MyList:
    def __init__(self,iterable = ()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __iter__(self):
        print('__iter__被调用')
        return MyListIterator(self.data)




class MyListIterator:

    def __init__(self,lst):
        self.data_lst = lst
        self.cur_index = 0

    def __next__(self):
        print('__next__被调用')
        if self.cur_index >= len(self.data_lst):
            raise StopIteration

        r = self.data_lst[self.cur_index]
        self.cur_index += 1
        return r


L = MyList([2,3,4,5])
# it = iter(L)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for i in L:
    print(i)