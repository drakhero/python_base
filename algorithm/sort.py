L = [2,4,7,3,1,8,2,2,6]

for i in range(0,len(L)):
    s=L[i]
    for j in range(i+1,len(L)):
        if s > L[j]:
            t = L[i]
            L[i] = L[j]
            L[j] = L[i]
            s = L[j]
print(L)
