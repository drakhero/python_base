def sort(a,n):
    if(n <= 1):
        return

    # 冒泡排序
    # for i in range(0,n):
    #     for j in range(n-i-1):
    #         if a[j] > a[j+1]:
    #             a[j],a[j+1] = a[j+1],a[j]

    #直接插入排序
    # for i in range(n):
    #     for j in range(i):
    #         if a[i] < a[j]:
    #             a.insert(j,a.pop(i))

    #希尔排序
    # sep = len(a)
    # while sep > 1:
    #     sep //= 2
    #     for i in range(sep,len(a)):
    #         for j in range(i%sep,i,sep):
    #             if a[i] < a[j]:
    #                 a[i],a[j] = a[j],a[i]

    #简单选择排序
    # for i in range(n):
    #     min_cur = i
    #     for j in range(i,n):
    #         if a[j] < a[min_cur]:
    #             min_cur = j
    #     a[i],a[min_cur] = a[min_cur],a[i]

    #归并排序






a = [2,6,3,8,1,4,2,9,5]
sort(a,len(a))
print(a)