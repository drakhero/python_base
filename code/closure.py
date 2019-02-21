# def make_power(y):
#     def fn(x):
#         return x**y
#     return fn
#
# pow = make_power(20)
#
# print(pow(2))
#
# def get_fx(a,b,c):
#     def fx(x):
#         return a*x**2 + b*x + c
#     return fx
#
# f123 = get_fx(1,2,3)
# print(f123(20))
# print(f123(50))


def fn(x):
    def f(ord):
        return 10 + x*(ord-1)
    return f


a = fn(2)
print(a(3))
print(a(5))








