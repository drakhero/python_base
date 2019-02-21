class Fibonacci:
    def __init__(self,n):
        self.number = n

    def __iter__(self):
        return Myiterator(self.number)

class Myiterator:
    def __init__(self,n):
        self.number = n
        self.one = 0
        self.two = 1
        self.count = 0

    def __next__(self):
        if self.count >= self.number:
            raise StopIteration
        while True:
            if self.count == 0:
                r = 1
            else:
                r = self.one + self.two
                self.one = self.two
                self.two = r
            self.count += 1
            return r


f = Fibonacci(10)
for i in f:
    print(i)

it = iter(f)
print(next(it))
print(next(it))
print(next(it))
print(next(it))