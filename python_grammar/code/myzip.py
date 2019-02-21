def myzip(*args):
    L = []
    for it in args:
        L.append(iter(it))
    while True:
        try:
            L2 = []
            for x in L:
                L2.append(next(x))
            yield tuple(L2)

        except StopIteration:
            break




for x,y,z,f in myzip("ABC","123","dkfl","78"):
    print(x,y,z,f)
