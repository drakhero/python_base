from threading import Event

e = Event()

e.set()
print(e.is_set())
e.clear()
print(e.is_set())


e.wait(2)

print("******************")