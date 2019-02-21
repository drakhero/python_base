class A:
    # 自定义类中加入了__enter__和__exit__方法才可以使用with语句

    def __enter__(self):
        print("在with语句内执行的")
        return  self
    #退出with语句时exit一定会执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        :param exc_type: 绑定错误类型，没有异常时绑定None
        :param exc_val: 绑定错误对象，没有异常时绑定None
        :param exc_tb: 绑定TraceBack对象，当没有异常时绑定None
        '''
        if exc_type is None:
            print("您已离开with语句,离开时没有发生任何异常")
        else:
            print("您已离开with语句")
            print("错误类型",exc_type)
            print("obj:",exc_val)
            print("Traceback:",exc_tb)

with A() as a:
    print("这是with语句内部的输出")
    int(input())

print("finally")


