def myenumerate(iterable,start = 0):
    for i in range(start,len(iterable)):
        yield i,iterable[i]


d = dict(myenumerate('abcde',1))
print(d)
