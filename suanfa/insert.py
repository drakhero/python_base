L = [13,10,1,5,8,2,9,3,4,6,7,11,12]

def insert(L):
    for i in range(1,len(L)):
        flag =L[i]
        for j in range(i-1,-2,-1):
            if flag<L[j]:
                L[j+1]=L[j]
            else:
                break
        L[j+1] = flag

insert(L)
print(L)


