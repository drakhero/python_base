def myyield():
    print("即将生产２")
    yield 2
    print("即将生产３")
    yield 3
    print("即将生产５")
    yield 5
    print("即将生产７")
    yield 7
    print("生成器生成结束")

s = myyield()
it = iter(s)
while True:
    try:
        r = next(it)
        print(r)
    except StopIteration:
        print("迭代结束")
        break