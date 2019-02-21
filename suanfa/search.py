#顺序查找
# def linear(value,key):
#     for x in range(len(value)):
#         if value[x] == key:
#             return x
#     else:
#         return -1
#
# values = [3,6,9,12,1,4,13,2,5,7,8,10,11]
#
# key = 7
#
# res = linear(values,key)
# if res == -1:
#     print("查找失败")
# else:
#     print("查找成功")



#二分法
# def divde(values,key):
#     start = 0
#     end = len(values)
#     while start != end:
#         mid = (start+end)//2
#         if key==values[mid]:
#             return mid
#         elif key > values[mid]:
#             start = mid + 1
#         else:
#             end = mid
#     else:
#         return -1

#递归
def divde(values,key,start,end):
    index = (start+end)//2

    if values[index] == key:
        return index
    elif values[index] < key:
        start = index + 1
    else:
        end = index
    if start == end:
        return -1

    return divde(values,key,start,end)

values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
key = 14

res = divde(values,key,0,len(values))
if res == -1:
    print("查找失败")
else:
    print("查找成功",res)
