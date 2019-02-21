import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",\
                     database="danei",charset='utf8',port=3306)

cursor = db.cursor()

# try:
#     insert_str = "insert into sheng values(12,500000,'辽宁省');"
#     drop_str = "delete from sheng where id=8"
#     update_str = "update sheng set s_name='浙江省' where id=1;"
#
#     cursor.execute(insert_str)
#     cursor.execute(drop_str)
#     cursor.execute(update_str)
#
#     db.commit()
#     print('ok')
# except Exception as e:
#     db.rollback()
#     print("Failed",e)

try:
    s_name = input("请输入省份：")
    s_id = input("请输入该省编号：")
    sql_insert = "insert into sheng(s_name,s_id) values(%s,%s);"

    L = [s_name,s_id]
    cursor.execute(sql_insert,L)
    db.commit()
    print("ok")
except Exception as e:
    db.rollback()
    print("Failed",e)

cursor.close()
db.close()