#账户管理系统服务器端

from socket import *
import pymysql


db_host = "127.0.0.1" #数据库服务器ｉｐ
db_user = "root" #用户名
db_passwd = "123456"
db_name = "test"#数据库名

address = ("0.0.0.0",9999)

db_conn = None #数据库连接对象

def conn_database():    #连接数据库
    global db_conn
    db_conn = pymysql.connect(db_host,db_user,db_passwd,db_name,charset='utf8')
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
    global db_conn
    resp = ''
    cursor = db_conn.cursor()
    if msgs[1] == "all": #查询所有
        sql = "select * from acct"
    else :
        sql = "select * from acct where acct_no='%s'" % msgs[1]

    print(sql)

    try:
        if cursor.execute(sql) < 1:  #执行查询
            resp = "没有该账号"

        else:
            result = cursor.fetchall()
            for row in result:
                acct_no = row[0]    #账号
                acct_name = row[1]    #户名
                balance = row[4]    #余额\
                acct_info = "账号：%s, 户名：%s,　余额：%.2f\n" % (acct_no,acct_name,balance)

                resp += acct_info   # 每一笔数据追加到响应信息后面

    except:
        print("查询错误")
    cursor.close()
    return resp #返回查询结果

def insert(msgs):
    cursor = db_conn.cursor()
    sql = "insert into acct values(%s,'%s',%s,%s,%s)" % (msgs[1],str(msgs[2]),msgs[3],msgs[4],msgs[5])
    print(sql)
    try:
        cursor.execute(sql)
    except:
        db_conn.rollback()
        return "插入失败"
    db_conn.commit()
    cursor.close()
    return "插入成功"

def update(msgs):
    cursor = db_conn.cursor()
    sql = "update acct set balance=%s where acct_name='%s'" % (msgs[2],msgs[1])
    print(sql)
    try:
        cursor.execute(sql)
    except:
        db_conn.rollback()
        return "更新失败"
    db_conn.commit()
    cursor.close()
    return "更新成功"


def delete(msgs):
    cursor = db_conn.cursor()
    sql = "delete from acct where acct_name='%s'" % msgs[1]
    print(sql)
    try:
        cursor.execute(sql)
    except:
        db_conn.rollback()
        return "删除失败"
    db_conn.commit()
    cursor.close()
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