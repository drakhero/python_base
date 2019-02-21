from threading import Thread,Event


s = None

def python():
    global s
    s = "我待python如初恋"
    print(s)
    e.set()

if __name__ == "__main__":
    e = Event()
    t = Thread(target=python)
    t.start()
    print("主线程：python虐我千百遍")
    e.wait()
    if s == "我待python如初恋":
        print("恭喜，薪资过万")
    else:
        print("下个班在等你")
    t.join()