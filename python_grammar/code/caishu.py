import random
x = random.randrange(0,100)

y = int(input("请猜一个数：　"))
while True:
    if y>x:
        y = int(input("猜大了"))
        continue
    if y<x:
        y = int(input("猜小了"))
        continue
    if y == x:
        print("猜对了")
        break