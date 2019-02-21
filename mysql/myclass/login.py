from MysqlPython import MysqlHelp

#加密模块
from hashlib import sha1

username = input("请输入用户名：　")
password = input("请输入密码：　")

#给password 加密
s1 = sha1() #创建sha1加密对象
s1.update(password.encode("utf-8")) #转码
password = s1.hexdigest() #返回十六进制加密结果

mysql = MysqlHelp("danei")
sql_select = "select password from user where \
             username=%s;"
psw = mysql.getAll(sql_select,[username])

if len(psw) == 0:
    print("用户名不存在")

elif password == psw[0][0]:
    print("ok")

else:
    print("密码错误")

