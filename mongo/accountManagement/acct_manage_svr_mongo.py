#账户管理系统服务器端

from socket import *
import pymongo

address = ("0.0.0.0",9999)
db_conn = None #数据库连接对象


db_host = "127.0.0.1" #数据库服务器ｉｐ
db_port = 27017
db_name = "test"#数据库名


def conn_database():    #连接数据库
    global db_conn
    db_conn = pymongo.MongoClient(db_host,db_port)
    if not db_conn:
        print("连接数据库失败")
        return -1
    else:
        return 1

def close_database(): #关闭数据库连接
    if not db_conn:
        return
    else:
        db_conn.close()

def query(msgs):    #执行查询
   qry = ""
   if msgs[1] == 'all':
       qry={}
   else:
       qry = {"acct_no":msgs[1]}
   print(qry)

   resp = ""
   try:
        mydb = db_conn[db_name]
        mycol = mydb['acct']

        docs = mycol.find(qry)
        for doc in docs:
            acct_info = "账户：%s, 户名:%s, 余额:%f\n"%(doc["acct_no"],doc["acct_name"],doc["balance"])
            resp += acct_info #将字符串追加到返回结果
   except Exception as e:
       print(e)
       print("查询异常")
   return  resp




def insert(msgs):
    dict = {
        'acct_no':msgs[1],
        'acct_name':msgs[2],
        'acct_type':msgs[4],
        'balance':float(msgs[5]),
    }

    try:
        mydb = db_conn[db_name]
        mycol = mydb["acct"]

        mycol.insert(dict)

    except:
        return "插入失败"
    return "插入成功"

def update(msgs):

    qry={"acct_name":msgs[1]}
    new_value = {'$set':{'balance':float(msgs[2])}}
    print(new_value)
    try:
        mydb = db_conn[db_name]
        mycol = mydb['acct']
        mycol.update(qry,new_value)
    except:
        return "更新失败"

    return "更新成功"


def delete(msgs):
    qry = {"acct_name":msgs[1]}

    try:
        mydb = db_conn[db_name]
        mycol = mydb['acct']
        mycol.delete_one(qry)
    except:
        return "删除失败"
    return "删除成功"



def main(): #服务器主程序
    if conn_database() == -1:  #首先连接数据库
        return  #连接失败，返回
    server = socket()
    server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    server.bind(address)
    server.listen(5)
    print("服务器已启动")
    sockfd,addr = server.accept()
    while True:
        data = sockfd.recv(2048)
        if not data:
            print("客户端已关闭")
            break

        #解析，分发
        print(data.decode())
        msgs = data.decode().split("::")    #按分隔符拆分
        if msgs[0] == "query":  #查询
            result = query(msgs)
            print(result)
        elif msgs[0] == "new":   #创建
            result = insert(msgs)
        elif msgs[0] == "update":    # 修改
            result = update(msgs)
        elif msgs[0] == "delete":  # 删除
            result = delete(msgs)
        else:
            print("非法操作请求")
        sockfd.send(result.encode())#发送结果至客户端
    close_database()    # 循环退出时关闭数据库
    server.close()

main()