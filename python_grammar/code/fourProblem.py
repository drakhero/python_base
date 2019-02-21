a = input()
b = input()
c = input()
d = input()
r = {a,b,c,d}
L = []
for i in r:
    for j in r-{i}:
        for k in r-{i,j}:
            s = i+j+k
            L.append(s)
print(L)


