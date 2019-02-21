
f = lambda n : True if (pow(n,2)+1)%5 == 0 else False

print(f(3))
print(f(4))

mymax = lambda a,b : a if a>b else b

print(mymax(100,200))