# def myeven(start,stop):
#     while start<=stop:
#         if start % 2 == 0:
#              yield start
#         start += 1
#
# for x in myeven(1,10):
#     print(x)
# L = [x**2 for x in myeven(1,20)]
# print(L)


def myfactorial(n):
    s = 1
    for x in range(1,n+1):
        s *= x
        yield s

L = list(myfactorial(5))
print(L)

print(sum(myfactorial(5)))