# n = int(input())
#
# print(" "*(n+3)+"*")
# print(" "*(n+2)+"*"*3)
# print(" "*(n+1)+"*"*5)
# print(" "*n+"*"*7)


#s = input()
# str = ''
# for i in s:
#     if i != ' ':
#        str += i
# print(str,len(str))

#str = s.replace(' ','')
#print(str,len(str))


a = 'hello!'
b = "I'm studying python"
c = "I like python"
n = 20
print("+"+"-"*n+"+")
# print("|"+" "*((20-len(a))//2) + a + " "*((20-len(a))//2) +"|")
# print("|"+" "*((20-len(b))//2) + b + " "*((20-len(b))//2+1) +"|")
# print("|"+" "*((20-len(c))//2) + c + " "*((20-len(c))//2+1) +"|")
print("|"+a.center(n)+"|")
print("|"+b.center(n)+"|")
print("|"+c.center(n)+"|")
print("+"+"-"*n+"+")