# L = list(range(10,20))
# for x in L:
#     print(x)
#     L.remove(x)
# print(L)


# begin = int(input())
# end = int(input())
# L = [x for x in range(begin,end) if x%2 == 0]
# print(L)

L = []
n = int(input())
while n != 0:
    L.append(n)
    n = int(input())

L2 = [x for x in L if x>0]
L3 = [x for x in L if x<0]
print(L)
print(L2)
print(L3)

