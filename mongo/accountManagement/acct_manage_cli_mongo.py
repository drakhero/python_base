'''数据格式
查询：
    请求：
        query::all  #查询所有账户信息
        query::622345000001 #查询指定账户

    响应：
        账号：622345000001,户名：Jerry,余额:10000

    新增：
        请求：
            new::522345000002::Tom::1::10.00
        响应：
            执行1笔操作
'''

from socket import *
import pymysql

client = None
host = "127.0.0.1"
port = 9999

def print_menu():
    menu = '''
    -------------账户管理------------
        1   -   查询账户
        2   -   新建账户
        3   -   修改账户
        4   -   删除账户
        5   -   退出
    '''
    print(menu)


def open_conn():    #连接到后台服务器的
    try:
        global client
        client = socket()
        client.connect((host,port))
        print("连接服务器成功")
        return 0
    except:
        print("连接服务器失败")
        return -1

def send_msg(msg):  #向服务器端发送信息
    if not client:
        print("未连接")
        return -1
    n = client.send(msg.encode())   #调用socket发送
    return n

def recv_msg():
    if not client:
        return None
    data = client.recv(2048)    #调用socket接收
    return data

def query_acct():
    acct_no = input("请输入要查询的账号：")
    if not acct_no  != "":  #输入空串，查询所有
        msg = "query::all"
    else:
        msg = "query::" + acct_no  #根据账户查询
    if send_msg(msg)<0: #调用函数发送请求
        print("发送失败")
        return
    data = recv_msg() #接收查询结果

    if not data:
        print("查询失败")
    else:
        print(data.decode())#打印查询结果

def insert_acct():
    while True:
        acct_no = input("请输入新的账号：")
        if not acct_no:
            print("账号不能为空")
            continue
        acct_name = input("请输入新的账户名：")
        if not acct_name:
            print("账户名不能为空")
            continue
        reg_date = "date(now())"
        acc_type = input("请输入新账户的账户类型：")
        balance = input("请输入账户余额")
        msg = "new"+"::"+acct_no+'::'+acct_name+'::'+reg_date+'::'+acc_type+'::'+balance
        if send_msg(msg)<0:
            print("发送失败")
            return
        data = recv_msg()
        if not data:
            print("未返回插入成功的信息")
        else:
            print(data.decode())

        n = input("是否继续添加?　Y/y是,其他否")
        if n.lower() != 'y':
            break

def update_acct():
    acc_name = input("请输入您要修改的用户名：")
    if not acc_name:
        print("用户名不能为空")
    while True:
        balance = int(input("请输入余额:"))
        if balance<0:
            print("请输入合法余额")
        else:
            break
    msg = "update"+"::"+acc_name+"::"+str(balance)
    if send_msg(msg)<0:
        print("发送失败")
        return
    data = recv_msg()
    if not data:
        print("未返回更新成功的信息")
    else:
        print(data.decode())



def delete_acct():
    acct_name = input("请输入要删除的账户名:")
    if not  acct_name:
        print("账户名不能为空")
    msg = "delete"+"::"+acct_name
    if send_msg(msg)<0:
        print("发送失败")
        return
    data = recv_msg()
    if not data:
        print("未返回删除成功的信息")
    else:
        print(data.decode())


def main():
    open_conn()
    while True:
        print_menu()
        oper = input("请输入要执行的操作:")
        if not oper:
            continue
        if oper == "1": #查询
            query_acct()
        elif oper == "2": #新增
            insert_acct()
        elif oper == "3":   #修改
            update_acct()
        elif oper == "4":   #删除
            delete_acct()
        elif oper == "5":   #退出
            break
        else:
            print("请输入正确的值")

main()


