a = float(input())
b = float(input())
c = float(input())

# min = a
# max = a
# if b<min:
#     max = min
#     min = b
# if c<min:
#     min = c
# if c>max:
#     max = c
# print("min:",min,"max",max)

min = a if a<b else b
min = c if min>c else min
print(min)


