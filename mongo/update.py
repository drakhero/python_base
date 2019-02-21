import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017")
dblist = conn.database_names()
dbname = "test"

if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb["acct"]
    query = {"acct_no":"622345000003"}
    new_value = {"$set":{"balance":9999.99}}
    ret = mycol.update_one(query,new_value,False,False)
    print("共修改%d笔"%ret.modified_count)

conn.close()