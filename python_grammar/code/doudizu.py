import random

L1 = ['\u2660','\u2663','\u2665','\u2666']
L2 = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

L = [x+y for x in L1 for y in L2]
L.extend(['POKER','poker'])

# random.shuffle(L)
k = 1
a = []
b = []
c = []
# d = []
# for i in L:
#     if k<=17:
#         a.append(i)
#     elif k<=34:
#         b.append(i)
#     elif k<=51:
#         c.append(i)
#     else :
#         d.append(i)
#     k += 1


p = L.copy()
while len(p)>3:
    ran = int(random.uniform(0,len(p)))
    if k % 3 == 1:
        a.append(p[ran])
    if k % 3 == 2:
        b.append(p[ran])
    if k % 3 == 0:
        c.append(p[ran])
    del p[ran]
    k += 1

def sorted_k(s):

    if s[-1] == 'R':
        return 17
    elif s[-1] == 'r':
        return 16
    elif s[-1] == '2':
        return 15
    elif s[-1] == 'A':
        return 14
    elif s[-1] == 'K':
        return 13
    elif s[-1] == 'Q':
        return 12
    elif s[-1] == 'J':
        return 11
    elif s[-1] == '0':
        return 10

    else:
        return int(s[-1])



input()
print(sorted(a,key=sorted_k))
input()
print(sorted(b,key=sorted_k))
input()
print(sorted(c,key=sorted_k))
input()
print(p)
