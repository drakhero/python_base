import sys

sys.stdout.write("我是一个标准输出\n")

sys.stderr.write("我的出现是个错误！！！\n")

print("hello",'world',file=sys.stdout)

f = open("myfile.txt",'w')
print("你好！","我在文件里",file=f)
f.close()
