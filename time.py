import time

old = time.mktime((2018,11,23,0,0,0,0,0,0))

now = time.time()

days = (now - old)/3600/24
print(days)
