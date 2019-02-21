x = 100
y = 200
s = 'x + y'

a = eval(s)

print(a)


b = eval(s,None,{"x":1,"y":2})
print(b)