from mysqlpython import MysqlPython

sqlh = MysqlPython("danei")

upd = "update t1 set t1name='C2' where t1name='B2'"

sqlh.execute(upd)

sql = "select * from t1"
print(sqlh.All(sql))