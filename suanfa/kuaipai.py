values = [13,10,1,5,8,2,9,3,4,6,7,11,12]

def quick(values):
    if len(values) < 2:
        return values
    key = values[0]
    #取出所有比key小的数据
    smaller = [x for x in values if x < key]
    #取出所有等于key的数字
    equal = [x for x in values if x == key]
    #取出所有比key大的数据
    big = [x for x in values if x > key]

    return quick(smaller) + equal + quick(big)

v = quick(values)
print(v)