import pymongo

db_conn = pymongo.MongoClient('localhost',27017)
dbname = 'jobs'

mydb = conn[dbname]
mycol = mydb['job']







db_conn.close()












