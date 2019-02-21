def read_numbers():
    L = []
    f = open('numbers.txt','rt')
    for x in f:
        L.append(int(x))
    f.close()
    return L

def print_numbers():
    L = read_numbers()
    print(max(L))
    print(min(L))
    print(sum(L))

print_numbers()