# def prime(begin,end):
#     for i in range(begin,end+1):
#         flag = True
#         for j in range(2,i):
#             if i % j == 0:
#                 flag = False
#                 break
#         if flag == True and i >= 2:
#             yield i
#
# for x in prime(10,20):
#     print(x)




def myxrange(start,stop,step=1):
    if step>0:
        while start < stop:
            yield start
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step
    else:
        print("step不能为0")

gen = (x**2 for x in range(10,1,-2))

for i in gen:
    print(i)













