import time
old = time.mktime((2019, 1, 15, 0, 0, 0, 0, 0, 0))

now = time.time()

days = (now - old)/3600/24
print(days)
