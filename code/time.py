import time

year = int(input())
month = int(input())
day = int(input())

birth = time.mktime((year,month,day,0,0,0,0,0,0))

now = time.time()

s = now - birth

print(s/3600/24)

t = time.localtime(now)

week = {
    0:"星期一",
    1:"星期二",
    2:"星期三",
    3:"星期四",
    4:"星期五",
    5:"星期六",
    6:"星期日"
}

print(week[t[6]])