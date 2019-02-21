from .MysqlPython import MysqlHelp

mysql = MysqlHelp("danei")

sql_select = "select * from sheng;"
result = mysql.getAll(sql_select)
print(result)


#7c4a8 d09ca 3762a f61e5 95209 43dc2 6494f 8941b