import pymongo
import bson.binary

from_img = "img.jpg"
to_img = "new.jpg"

def save_img(myset):#存文件
    f = open(from_img,"rb")
    data = f.read()
    #content = bson.binary.Binary(data) #格式转换
    myset.insert(
        {"filename": from_img,
        "data":data}
    )
    print("save successful")

def get_img(myset):
    img = myset.find_one({"filename":from_img+'1'})
    with open(to_img,"wb") as f:
        f.write(img["data"])
    print("save new file ok")
    return


conn = pymongo.MongoClient("mongodb://localhost:27017")
db = conn.gridfs
myset = db.image

#save_img(myset) #调用存文件函数
get_img(myset)

conn.close()