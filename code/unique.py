L = [1,2,3,6,6,6,2,3,7,8]
L2 = []
L3 = []
for i in L:
    if i not in L2:
        L2.append(i)

# for i in L:
#     c = L.count(i)
#     if c == 2 and i not in L3:
#         L3.append(i)
for i in L:
    c = 0
    for j in L:
        if i == j:
            c += 1
    if c == 2 and i not in L3:
        L3.append(i)

print(L2)
print(L3)



L = set(L)
L = list(L)
print(L)