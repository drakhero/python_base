import os
c = 0
n = 0

def count(path):
    file_list = os.listdir(path)
    #print(file_list)
    for file in file_list:
        # print(file)
        # print(os.path.isdir(path+'/'+file))
        if os.path.isdir(path+'/'+file):
            count(path+'/'+file)
        else:
            if file[-3:] == '.py':
                print(file)
                global n
                n += 1
                for index,line in enumerate(open(path+'/'+file,'r')):
                    global c
                    c += 1

if __name__ == "__main__":
    path = '/home/tarena/python'
    count(path)
    print(n)
    print(c)