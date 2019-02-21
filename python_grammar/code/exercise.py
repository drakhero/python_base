import filter

print(216//16,'斤',216%16,'两')

n = int(input())
for i in range(n-1,1,-1):
    print(" "*(n//2+1-i+10),end='')
    print("*"*(2*i+1))
for i in range(0, n):
    print(" "*(n//2+1-i+10),end='')
    print("*"*(2*i+1))

print(filter.iseven(3))