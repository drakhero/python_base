L = [5,-2,-4,0,3,1]
print(sorted(L,key=abs))

names = ['Tom', 'Jerry', 'Spike', 'Tyke']
def re(s):
    return s[::-1]

print(sorted(names,key = re))