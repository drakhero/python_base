from mysqlpython import MysqlPython

from hashlib import sha1

sqlh = MysqlPython("danei")

#让用户输入用户名
uname = input("请输入注册用户名：　")

#到user表中查询此用户信息
#sele = 'select username from user where username=%s'
#r = sqlh.All(sele,[uname])

# if len(r) != 0:
#     print("该用户已存在")
# else:
#     #输入密码
#     pwd1 = input("请输入密码: ")
#     pwd2 = input("请再次输入密码: ")
#
#     if pwd1 == pwd2:
#         #把密码加密存入数据库
#         #创建加密对象
#         s = sha1()
#         #加密，参数一定要为ｂｙｔｅｓ数据类型
#         s.update(pwd1.encode("utf-8"))
#         #返回十六进制加密结果
#         pwd = s.hexdigest()
#         ins = 'insert into user values(%s,%s)'
#         sqlh.execute(ins,[uname,pwd])
#         print("注册成功")
#     else:
#         print("两次密码不一致")


#用户登录
sele = "select password from user where username=%s"
r = sqlh.All(sele,[uname])
pwd = input("请输入密码：　")

s = sha1()
s.update(pwd.encode("utf-8"))
pwd = s.hexdigest()
if len(r) == 0:
    print("用户名错误")
elif pwd == r[0][0]:
    print("登录成功")
else:
    print("密码错误")