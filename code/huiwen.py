
s = input()
# flag = True
# if len(s) % 2 == 0:
#     if s[:len(s)//2:] != s[len(s)-1:len(s)//2+1:]:
#         flag == False
# else:
#     if s[:len(s)//2:] != s[len(s)-1:len(s)//2:]:
#         flag == False
#
# print(flag)

if s == s[::-1]:
    print(True)
else:
    print(False)