
def mymax(a,*args):
    max = 0
    if type(a) == type(0) or type(a) == type(0.0):
        max = a
        for i in args:
            if i>max:
                max = i
    if type(a) == type([]):
        max = a[0]
        for i in a:
            if i>max:
                max = i
    return max

print(mymax(1))