def myinteger(n):
    i = 0
    while i<n:
        yield i
        i += 1

for x in myinteger(3):
    print(x)

L = [x for x in myinteger(100) if x % 2 == 1]
print("L =", L)
