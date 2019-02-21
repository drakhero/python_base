import  pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017")
dblist = conn.database_names()

dbname = "test"
if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb["acct"]

    #插入数据
    mydata = [
        {"acct_no":"622345777777",
         "acct_name":"Keven",
         "balance":3333.33},
        {"acct_no":"622345666666",
         "acct_name":"Michle",
         "balance":4444.44},
        {"acct_no":"622345555555",
         "acct_name":"Lucy",
         "balance":5555.55}
    ]
    ret = mycol.insert_many(mydata)
    print(ret.inserted_ids)#打印所有新ID

conn.close()