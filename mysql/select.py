from pymysql import connect

db = connect(host="localhost",user="root",password="123456",\
             database="danei",charset='utf8',port=3306)

cursor = db.cursor()

sql_select = "select * from sheng"
sql = "insert into sheng(id) values(40),(50),(60)"
n = cursor.execute(sql)#所有的数据都放入了cursor对象中

print(n)
# data1 = cursor.fetchone()
# print(data1)
# print("*"*50)
#
# data2 = cursor.fetchmany(3)
# print(data2)
# print("*"*50)
#
# data3 = cursor.fetchall()
# # print(data3)

cursor.close()
db.close()
