f = open('myflush.txt','w')
f.write('aaa')
#缓冲区,通过控制io操作次数提高执行效率
# while True:
#     f.write('aaaaaa'*100)
#     time.sleep(1)
#     print("写入一次...")
f.flush() #强制将缓冲区的内容写到磁盘上

s = input("请输入回车键继续：　")

f.close()