import pymysql
#创建数据库连接对象
db = pymysql.connect(host="localhost",\
                     user="root",password="123456",\
                     database="danei",charset="utf8")

#利用db创建游标对象
cursor = db.cursor()

#利用cursor的execute()方法执行SQL命令
sql_insert = "insert into sheng values(30,400000,'吉林省');"
cursor.execute(sql_insert)

#提交到数据库执行
db.commit()

#关闭游标对象
cursor.close()

#断开数据库连接

db.close()
