#查询示例
import pymongo

#创连接对象
#conn = pymongo.MongoClient(host="localhost",port=27017)
conn = pymongo.MongoClient("mongodb://localhost:27017")

#获取数据库对象
dblist = conn.database_names()
dbname = "test"
if dbname in dblist:
    mydb = conn["test"] #获取数据库对象,相当于ues test
    mycol = mydb["acct"] #获取集合对象
    #query = {} #不带筛选条件查询
    #query = {"acct_no":"622345000005","acct_name":"Lmma"}
    #query = {"balance":{"$gt":5000}} #余额大于5000的
    query = {"$or":[{"acct_name":"Daniel"},{"acct_name":"Emma"}]}

    #project = {"_id":0} #不显示_id域
    project = {"_id":False,"acct_no":True,"acct_name":True,"balance":True}

    docs = mycol.find(query,project) #执行查询

    #取指定域
    for doc in docs:
        #print(doc)
        acct_info = "账号:%s,　户名:%s, 余额:%f" % (doc["acct_no"],doc["acct_name"],doc["balance"])
        print(acct_info)


conn.close()
