import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017")
dblist = conn.database_names()

dbname = "test"

if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb['acct']

    mydict = {
        "acct_no":"622345888888",
        "acct_name":"David",
        "balance":3333.33
    }

    ret = mycol.insert_one(mydict) #执行插入

    print("NewId:",ret.inserted_id)

conn.close()