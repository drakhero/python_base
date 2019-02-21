import pymongo
import re

# class mongo:
#     def __int__(self,database,host='localhost',port=27017):
#         self.host = host
#         self.port = port
#         self.db = database
#
#
#     def connMongo(self):
#         db_conn = pymongo.MongoClient(self.host,self.port)
#
#     def colse_mg(self):
#         db_conn.close()

db_conn = pymongo.MongoClient("mongodb://localhost:27017")
db_name="jobs"
try:
    mydb = db_conn[db_name]
    mycol = mydb['job']
except:
    print("出错了")
i=0
head = ''
with open("lagou_jobs.csv") as f:
    head = f.readline()
    head_list = head.strip().split(',')
    print(head_list)
    while True:
        read_info = f.readline().strip()
        if read_info == '':
            break
        info = re.findall('([（）\w\(\)-]+),',read_info)
        #print(info)

        craft = re.findall('\"[^\[].*?\"',read_info)
        if  craft:
            craft[0] = craft[0].strip('\"')
            info[3] = craft[0]
        welfare = re.findall('\"(\[.*?\])\"|\[\]',read_info)
        grade = []
        grade.append(read_info[-2]+read_info[-1])
        info += grade
        # print(info)
        # print(welfare)
        info.insert(10,welfare[0])
        #print(craft)
        if len(info) == 1:
            break
        if len(info) != 12:
            continue
        print(info)
        i+=1
        print(i)



        dict={
            head_list[0]: info[0],
            head_list[1]: info[1],
            head_list[2]: info[2],
            head_list[3]: info[3],
            head_list[4]: info[4],
            head_list[5]: info[5],
            head_list[6]: info[6],
            head_list[7]: info[7],
            head_list[8]: info[8],
            head_list[9]: info[9],
            head_list[10]: info[10],
            head_list[11]: info[11]
        }
        mycol.insert_one(dict)


db_conn.close()




