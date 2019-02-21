# names = ['中国移动','中国联通','中国电信']
#
# for t in enumerate(names):
#     print(t)
#
# for index,names in enumerate(names):
#     print("索引为",index,'的位置对应',names)
#
# for t in enumerate(names, 101):
#     print(t)


n = input()
L = []
while True:
    if not n:
        break
    L.append(n)
    n = input()
for index,value in enumerate(L,1):
    print("第{}行:{}".format(index,value))