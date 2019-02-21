s = "3094333@qq.com aaa@126.com 555555@qq.com"

#用split方法进行分割
# rList = s.split()
# for r in rList:
#     if r[-6:] == "qq.com":
#         print(r)

import  re

s = re.findall('[0-9a-z]+@[0-9a-z]+.com',s)
print(s)