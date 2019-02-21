import re

#提取ip地址
# s = '192.168.1.111上海长寿路中心 192.168.1.112深圳福永中心　192.168.1.113杭州西湖中心 192.168.1.114成都奥克斯中心'
#
# r = re.findall('[0-9a-zA-Z_]',s)
# print(r)



# s = 'hello 13811111111 I am 1399999999,He is 119 hello 119'
# rList = re.findall('hello',s)
# print(rList)


#元字符

# with open("passwd") as f:
#     result = []
#     while True:
#         s = f.readline()
#         if not s :
#             break
#         result += re.findall('^tarena.*',s)
#
# print(result)

#统计没有登录权限的用户数量
# with open("passwd") as f:
#     result = []
#     i=0
#     while True:
#         s = f.readline()
#         if not s :
#             break
#         r = re.findall('.*/usr/sbin/nologin$',s)
#         result += re.findall('.*/usr/sbin/nologin$', s)
#         if r:
#             i+=1
#
# print(result)
# print(i)


# s = '''
#     Link encap:以太网  硬件地址 00:0c:29:22:57:72
#           inet 地址:10.8.31.247  广播:10.8.31.255  掩码:255.255.255.0
#           inet6 地址: fe80::b40d:7080:1421:46a3/64 Scope:Link
#           UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
#           接收数据包:149823 错误:0 丢弃:0 过载:0 帧数:0
#           发送数据包:21165 错误:0 丢弃:0 过载:0 载波:0
#           碰撞:0 发送队列长度:1000
#           接收字节:26919997 (26.9 MB)  发送字节:1904545 (1.9 MB)
#
# '''
# result = re.findall('[0-9a-z]{2}\:[0-9a-z]{2}\:[0-9a-z]{2}\:[0-9a-z]{2}\:[0-9a-z]{2}\:[0-9a-z]{2}',s)
# print(result)


# s = "3094@qq.comwang@126.comwei@163.commeng@tedu.cn"
#
# com = re.findall('[a-z0-9A-Z]+@[a-z0-9A-Z]+\.com',s)
#
# comcn = re.findall('\w+@\w+\.com|\w+@\w+\.cn',s)
#
# print(com)
# print(comcn)





# s = """
# <div>仰天大笑出门去</div>
# <div>九霄龙吟惊天变</div>
# """
# #贪婪匹配
# result = re.findall('<div>[\s\S]*</div>',s)
# print(result)
#
# r = re.findall('<div>([\s\S]*?)</div>',s)
# print(r)


# s = 'A B C D'
# r1 = re.findall('\w+\s+\w+',s)
# print(r1)
#
# r2 = re.findall('(\w+)\s+\w+',s)
# print(r2)
#
# r3 = re.findall('(\w+)\s+(\w+)',s)
# print(r3)
#
# r4 = re.findall('((\w+)\s+)(\w+)',s)
# print(r4)






# pattern = r'\w+:\d+'
# s = '金毛狮王:1950 紫衫龙王:1949'
#
# rList = re.findall(pattern,s)
# print(rList)
#
# regex = re.compile(pattern)
# rList = regex.findall(s,pos=5,endpos=30)
# print(rList)




# regex = re.compile('\s+')
# rSplit = regex.split('hello world hello tarena')
# print(rSplit)



# regex = re.compile(r'\s+')
# rSub = regex.sub('###','hello world hello',1)
# print(rSub)


# rIter = re.finditer(r'\d+','2019来了,2018啥也没干')
# print(next(rIter))
# for r in rIter:
#     print(r.group())


# rMatch = re.match(r'[A-Z]\w+','Hello world')
# print(rMatch.group())


rGroup = re.search(r'(?P<monkey>\w+)\s+(?P<elephant>\w+)','A B C D')
print(rGroup.group(2))




















