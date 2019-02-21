# s = input()
# d = {}
# for x in s:
#     if x in d.keys():
#         d[x] += 1
#     else:
#         d[x] =1
#
# print(d)

nos = [1001,1002,1005,1008]
names = ['Tom','Jerry','Spike','Tyke']
d = {}
for i in range(0,len(nos)):
    d[nos[i]] = names[i]

print(d)