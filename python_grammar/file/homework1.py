def productList():
    L = []
    while True:
        n = int(input())
        if n < 0 :
            break
        L.append(str(n))
    return L

def input_file():
    f = open('numbers.txt','wt')
    for s in productList():
        f.write(s+'\n')
    f.close()

input_file()