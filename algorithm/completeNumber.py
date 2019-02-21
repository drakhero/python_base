import math
L =[2]
# def prim(begin,end):
#     e = math.ceil(math.sqrt(end))+1
#     for x in range(begin, e):
#         for y in L:
#             if x % y == 0:
#                 break
#         else:
#             L.append(x)
# def wqs():
#
#         prim(3,20000000000)
#         for p in L:
#             if (pow(2,p)-1) in L:
#                 print((pow(2,p)-1)*pow(2,p-1))
# wqs()




def is_prim1(num):
    e = math.floor(math.sqrt(num)) + 1
    if num == 2: return True

    for x in L:
        if x < e:
            if num % x == 0:
                    return False
            else:
                if num not in L :
                    L.append(num)
                return True
L2 = [2]
def is_prim2(num):
    e = math.floor(math.sqrt(num)) + 1
    for i in range(L2[len(L2)-1],e):
        for j in L2:
            if i % j == 0:
                break
            else:
                L2.append(i)
                break
    for k in L2:
        if num % k == 0:
            return False
    else:
        return True

for p in range(2, 100000000):
    if is_prim1(p) and is_prim2(pow(2, p)-1):
        print((pow(2, p) - 1) * pow(2, (p - 1)))


# def is_prime(num):
#     if num == 2 : return True
#     for i in range(2,math.floor(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     else:
#         return True

# for p in range(2, 1000000000000000000000000):
#     if is_prim1(p) and is_prime(pow(2, p)-1):
#         print((pow(2, p) - 1) * pow(2, (p - 1)))

# L3 = [2,3]
# def pr():
#     for x in range(4, 700):
#         for y in L3:
#             if x % y == 0:
#                 break
#         else:
#             L3.append(x)
# pr()
# flag = True
# for p in range(2, 10):
#     for i in L3:
#         if p<i and p % i == 0:
#             flag = False
#         if pow(2,p)-1<i and (pow(2,p)-1)%i == 0:
#             flag = False
#     if flag:
#         print((pow(2, p) - 1) * pow(2, (p - 1)))