numbers = [10086,10000,10010,95588]
names = ['中国移动','中国联通','中国电信']
for t in zip(numbers,names):
    print(t)

def myzip(iter1,iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    while True:
        t = (next(it1),next(it2))
        yield t

for t in myzip(numbers,names):
    print(t)
