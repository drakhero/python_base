import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017")
dblist = conn.database_names()

dbname = "test"

if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb["acct"]
    query = {}
    #project = {"_id":0,"acct_name":1,"balance":1}

    docs = mycol.find(query) # 执行查询
    sortedDocs = docs.sort([("balance",pymongo.ASCENDING)])

    for doc in sortedDocs:
        acct_info = "账号：%s, 户名：%s, 余额：%f" % (doc['acct_no'],doc['acct_name'],doc['balance'])
        print(acct_info)
        