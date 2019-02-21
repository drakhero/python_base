from mysql_db import sql_execute

def stu_add():
    s = input("请输入学生name,age:")
    name,age = s.strip().split(',')
    sql = "insert into stu(name,age) values(%s,%s)"
    sql_execute(sql,[name,int(age)])

def stu_delete():
    name = input("请输入要删除的学生姓名：　").strip()
    sql = "delete from stu where name=%s"
    sql_execute(sql,[name])
