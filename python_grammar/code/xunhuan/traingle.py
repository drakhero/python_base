n = int(input())

i = 1
while i<=n:
    print("*"*i)
    i += 1

print()

i = 1
while i<=n:
    print(" "*(n-i)+"*"*i)
    i += 1

print()

i = n
while i>0:
    print("*"*i)
    i -= 1

print()

i = n
while i>0:
    print(" "*(n-i)+"*"*i)
    i -= 1




