# for i in range(1,21):
#     print("%4d"%i, end='')


# for  i in range(1,21):
#     print("%4d" % i,end='')
#     if i%5 == 0:
#         print()

# n = int(input())

# for i in range(0,n):
#     if i % 2 == 0:
#         print("%3d"%i,end='')

begin = int(input())
end = int(input())
i = 0
while begin<end:
    print(begin,end='   ')
    begin+=1
    i += 1
    if i%5 == 0:
        print()

