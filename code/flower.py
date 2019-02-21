# n = int(input())
#
# for i in range(1,2*n+1):
#     if i<=n:
#         print(" "*(2*n-i)+"*"*(2*i-1))
#     else:
#         print(" "*(2*n-1)+"*")


# L = []
# for i in range(100,999):
#     if pow(i//100,3)+pow((i//10)%10,3)+pow(i%10,3) == i:
#         L.append(i)
# print(L)

# import math
n = int(input())
if n>1:
    for i in range(2,n//2):
        if n % i == 0:
            print("不是素数")
            break
    else:
        print("是素数")
else:
    print('不是素数')

