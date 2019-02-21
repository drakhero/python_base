def privivlege_check(fn):
    print("aaaaaaaaaaaaaa")
    def fx(name, x):
        print("正在进行权限验证......")
        if True:
            fn(name,x)
        else:
            print("权限验证失败")
    return  fx

def message_send(fn):
    def fy(n,money):
        fn(n,money)
        print("正在发送短信...",n,'...')
    return  fy

@message_send
@privivlege_check
def savemoney(name,x):
    print(name,'存钱',x,'元')
# 实质：
# savemoney = privivlege_check(savemoney)
# savemoney = message_send(savemoney)



@message_send
@privivlege_check
def withdraw(name,x):
    print(name, '取钱', x, '元')

savemoney('小李',100)
savemoney('小李',100)
savemoney('小李',100)
savemoney('小刚',300)
withdraw('小张',200)

