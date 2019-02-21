import  random

L = [chr(x) for x in range(65,91)]
L += [chr(x) for x in range(97,123)]
L += [str(x) for x in range(0,10)]

code = random.sample(L,6)
print(''.join(code))



s = ''
for i in range(0,6):
    s += random.choice(L)

print(s)