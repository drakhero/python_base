L = [2,3]
# flag = True
# for x in range(4,100):
#     for y in L:
#         if x%y == 0:
#             flag = False
#             break
#         else:
#             flag = True
#     if flag:
#         L.append(x)
# print(L)

for x in range(4,100):
    for y in L:
        if x%y == 0:
            break
    else:
        L.append(x)
print(L)


