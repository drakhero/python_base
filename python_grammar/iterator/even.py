def even(start, stop):
    while start<stop:
        if start % 2 == 0:
            yield start
        start += 1


for x in even(1,10):
    print(x)

L = [x**2 for x in even(10,20)]
print(L)

it = iter(even(3,10))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
