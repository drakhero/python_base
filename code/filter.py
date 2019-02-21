import  math

def iseven(x):
    return x % 2 == 0

L=list(filter(iseven,range(1,21)))
print(L)


S = []
def prime(x):
    if x<2:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i == 0:
            return False
    else:
        return True

S.extend(filter(prime,range(1,101)))
print(S)