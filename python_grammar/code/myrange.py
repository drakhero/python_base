
def myrange(start, end=None, seq=1):
    try:
        s = 1/seq
        if end == None:
            end = start
            start = 0
        if seq > 0:
            while start<end:
                yield start
                start += seq
        if seq < 0:
            while start>end:
                yield start
                start += seq
    except StopIteration:
        print("循环结束")
    except ZeroDivisionError:
        print("第三个参数不能为零")

for i in myrange(0,10):
    print(i)
