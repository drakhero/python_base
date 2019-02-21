# h = 100
# n = int(input())
# s = 0
# i = 0
# while i<n:
#     i += 1
#     s += h
#     h /= 2
# print("第{}次落地反弹高度{}米".format(n,h))
# print("经过了",s,"米")


n = int(input())

def is_Prime(n):
    if n > 1:
        for i in range(2, n // 2):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

def primNumber(n,L):
    if n < 2:
        return
    for i in range(2,n//2+1):
        if n % i == 0:
            L.append(i)
            if is_Prime(n//i):
                L.append(n//i)
            return primNumber(n//i,L)

L = []
if is_Prime(n):
    L.append(n)
primNumber(n,L)
print(L)
