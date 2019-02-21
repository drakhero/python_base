def div_apple(n):
    print("%d个苹果您想分给几个人？" % n)
    s = input('请输入人数：')
    cnt = int(s)
    result = n / cnt
    print("每个人分了",result,'个苹果')

try:
    div_apple(10)
    print("分苹果完成")
except (ValueError,ZeroDivisionError):
    print("生气了,不分了")
except:
    print('收到')
# except ValueError:
#     print("在try的内部语句中发生了异常,已处理并转为正常状态")
# except ZeroDivisionError:
#     print("输入错误")

print("程序正常退出")