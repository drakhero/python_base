def get_chinese_char_count(x):
    count = 0
    for ch in x:
        if ord(ch) > 127:
            count += 1
    return  count

s = input("请输入中英混合的字符串：　")
print("中文字符个数：　",get_chinese_char_count(s))