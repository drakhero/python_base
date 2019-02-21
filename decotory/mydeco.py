def mydeco(fn):
    def fx():
        print("fx被调用")
        fn()
    return fx

@mydeco
def myfun():
    print("myfun被调用")

myfun()
