
s1 = ''
s2 = ''
i = 65
while i<91:
    s1 += chr(i)
    s2 += chr(i)
    s2 += chr(i+32)
    i += 1
print(s1)
print(s2)