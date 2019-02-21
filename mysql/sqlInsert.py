import pymysql
import hashlib

def md5(pwd):
    m = hashlib.md5()
    m.update(pwd.encode('utf-8'))
    return  m.hexdigest()

print(md5('14334'))

conn = pymysql.connect(host="localhost",user="root",password="123456",database="db4",charset="utf8",port=3306)


user_input_name = input('请输入账号:')
user_input_pwd = input('请输入密码:')


cursor = conn.cursor()

# sql = "select uid from user_ where "
# sql += "uname='"+user_input_name
# sql += "'and upwd='"
# sql += user_input_pwd
# sql += "'"
sql = "select uid from user_ where uname=%s and pwd=%s"

print(sql)

cursor.execute(sql,[user_input_name,user_input_pwd])

print(cursor.fetchone())


cursor.close()
conn.close()