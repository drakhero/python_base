# L = [1,3,5,6]
#
# #it = iter(range(1,10,3))
# it = iter(L)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break

s = {'唐僧','悟空', '八戒', '沙僧'}
it = iter(s)
while True:
    try:
        name = next(it)
        print(name)
    except StopIteration:
        print("遍历结束")
        break

