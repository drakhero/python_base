x = 100
y = 200

try:
    save_x = x
    save_y = y
    try:
        x = int(input("x:"))
        y = int(input("y:"))
        print(x,y)
    finally:
        x = save_x
        y = save_y
except:
    pass
print(x,y)
