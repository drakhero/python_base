import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017")
dblist = conn.database_names()
dbname = "test"

if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb["acct"]
    query = {"acct_no":"622345000003"}
    ret = mycol.delete_one(query)
    print("共删除%d笔"%ret.deleted_count)

conn.close()