class Prime:
    def __init__(self,b,n):
        self.begin = b
        self.count = n

    def __iter__(self):
        return Myiterator(self.begin,self.count)

class Myiterator:
    def __init__(self,b,n):
        self.begin = b
        self.c = n
        self.count = 0

    def __isPrime(self,num):
        if num < 2 :
            return False
        else:
            for i in range(2,num):
                if num % i == 0:
                    return False
            else:
                return True


    def __next__(self):
        if self.count >= self.c:
            raise StopIteration
        while True:
            if self.__isPrime(self.begin):
                self.count += 1
                r = self.begin
                self.begin += 1
                return r
            self.begin += 1


p = Prime(1,100)
for i in p:
    print(i)
it = iter(p)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))