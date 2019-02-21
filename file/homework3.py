# def copy_file():
#     f_origin = open('mybinary.bin','rb')
#     f_copy = open('mybinaryCopy.bin','wb')
#
#     for s in f_origin:
#         f_copy.write(s)
#
#
#     f_origin.close()
#     f_copy.close()
#
# copy_file()

def mycopy(src_filename,dst_filename):
    try:
        fr = open(src_filename, 'rb')
        try:
            try:
                fw = open(dst_filename,'wb')
                try:
                    while True:
                        b = fr.read(4096)
                        if not b:
                            break
                        fw.write(b)
                finally:
                    fw.close()
            except OSError:
                print("目标文件打开失败")
        finally:
            fr.close()
    except OSError:
        print("源文件打开失败")

mycopy('mybinary.bin','mybinaryCopy.bin')