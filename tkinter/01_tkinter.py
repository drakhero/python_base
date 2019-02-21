from tkinter import *
root = Tk()
root.geometry('400x400+300+100')

def click():
    print("ll")

Button(root,text='点我有惊喜',command=click,bg='red').pack(fill=X,expand=2,padx=100,pady=24)
Button(root,text='点我有惊喜',command=click,bg='red').pack(fill=X,expand=2)
Button(root,text='点我有惊喜',command=click,bg='red').pack(fill=X,expand=0)
Button(root,text='点我有惊喜',command=click,bg='red').pack(fill=X,expand=0)

root.mainloop()
