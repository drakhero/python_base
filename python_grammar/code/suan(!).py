
def myfac(n):
    if n<2:
        return 1

    return n*myfac(n-1)

print(myfac(5))


def fun(n):
    result = 0
    s = ''
    for i in range(1,n+1):
        result += pow(i,2)
        if result != 1:
            s += "+" + str(i)+"*"+str(i)
        else:
            s += str(i)+"*"+str(i)
    s += " ="
    return s,result
print(fun(3)[0],fun(3)[1])


def yang(n):
    L = []
    L.append([1])
    for i in range(1,n):
        L.append([])
        L[i].append(1)
        for j in range(1,len(L[i-1])):
            L[i].append(L[i-1][j-1] + L[i-1][j])
        L[i].append(1)

    for k in L:
        s = ''
        for o in k:
            s += str(o) + ' '
        print(s.center(n*3))

yang(10)
print("\n")


L = [[3,5,8],10,[[13,14],15,18],20]
sum = 0
def print_list(lst):
    for i in lst:
        if type(i) is int:
            print("%3d"%i,end='')
        else:
            print_list(i)


s=0
def sum_list(lst):
    global s
    for i in lst:
        if type(i) is int:
            s += i
        else:
            sum_list(i)
    return s

print(sum_list(L))
print_list(L)














