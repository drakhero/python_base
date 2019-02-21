# gen = (x**2 for x in range(1,5))
# it = iter(gen)
#
# for i in range(0,4):
#     print(next(it))




L = [2,3,5,7]

# def mygen(L):
#     for x in L:
#         yield pow(x,2)+1
#
# y = mygen(L)
# for i in y:
#     print(i)
# print(y)
# s = list(y) #一个生成器只能使用一次
# print(s)


# for a in (x**2+1 for x in L):
#     print(a)

L2 = [x**2+1 for x in L]
it = iter(L2)
print(next(it))
L[1] = 30
print(next(it))

gen = (x**2 + 1 for x in L)
it = iter(gen)
print(next(it))
L[1] = 30
print(next(it))





















