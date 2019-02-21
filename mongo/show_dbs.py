#列出服务器上所有的数据库

import pymongo

#建立到服务器的连接: MongoClient
conn = pymongo.MongoClient(host="localhost",port=27017)

#列出所有库
dblist = conn.database_names()
if not dblist:
    print("dblist is none")
else:
    for db in dblist:
        print(db)
#关闭数据库
conn.close()