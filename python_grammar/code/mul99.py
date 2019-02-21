# #1
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(" {:>1}x{:>1}={:>2}".format(j,i,j*i),end='')
#     print()
# #2
# def print_aline(end):
#     for col in range(1,end+1):
#         print(" {:>1}x{:>1}={:>2}".format(col,end,col*end),end='')
#     print()
# def print_99():
#     for line in range(1,10):
#         print_aline(line)
#
# print_99()


# n = int(input())
# for i in range(1,n+1):
#     for j in range(i,n+i):
#         print(j,end='')
#     print()



n = int(input())

for i in range(2,n):

    # for j in range(1,i//2+1):
    #     if i%j == 0:
    #         L.append(j)

    if i%10==6 or i%10==8:
        L1 = [1]
        j = 2
        h = i
        while j<h:
            if i % j == 0:
                L1.append(j)
                L1.append(i//j)
                h = i // j
            j += 1
        if sum(L1) == i:
            print(i)














