# s = input()
#
# if len(s) != 0:
#     print(ord(s[0]))

# x = int(input())
# if x>=0 and x<=65535:
#     print(chr(x))

# def mysum(n):
#     if n<2:
#         return 1
#
#     return n+mysum(n-1)
#
# print(mysum(100))

# my_dict = {'name':'tom','age':6,'skill':'catch jerry'}
# #s = str(my_dict).replace('{','').replace('}','').replace(': ','=').replace(', ','|').replace('\'','')
# l = [y for x in list(my_dict.items()) for y in x ]
# L = '|'.join([k+'='+str(v) for k,v in my_dict.items()])
# print(my_dict.items())

# a = 12
# def my_func():
#     a = 10
#     def my_inner_func():
#         global a
#         a+=10
#         print(a)
#     my_inner_func()
# my_func()

# def f():
#     global a
#     a = 10
#
# f()
# print(a)
# def f(a):
#   return a[1]
# L = ['222','a13','A33']
# sorted(L,key=f)
# print(L)

# d = {}
# i = 0
# while True:
#   s = input()
#   if not s:
#     break
#   i += 1
#   d[i] = s
#
# for line,value in d.items():
#   print("第{}行:".format(line),value)


class A:
  v = 100
  def __init__(self):
    self.v = 200

a1 = A()
a2 = A()

del a2.v  #删除a2这个对象的属性v
print(a2.v)# 由于本身v被删除,所以到外部嵌套函数作用于找类中的v
print('v' in dir(a2))#True
del a2.__class__.v #删除类A的属性v
print('v' in dir(a2))#Flase




























