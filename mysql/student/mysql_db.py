import pymysql

def sql_execute(sql,L):
    db = pymysql.connect(host="localhost",user='root',password="123456",database="student_info",charset="utf8",port=3306)
    cur = db.cursor()

    cur.execute(sql,L)

    db.commit()

    cur.close()
    db.close()



