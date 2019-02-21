# L = []
# for i in range(0,40):
#     if i in (0,1):
#         L.append(1)
#     else:
#         L.append(L[i-2]+L[i-1])
# print(L)

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input())
L = []
for i in range(1,n+1):
    L.append(fib(i))

print(L)