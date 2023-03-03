from tkinter import *
win = Tk()
win.geometry("200x300")
def data():
    en.get()
def dele():
    tr = en.get()
    en.delete(0,str)
en = Entry(win, font="Arial 20", bg="white", bd=3, width=30)
en.place(x=20, y=20)
bt1 = Button(win, text="nhan")
bt1.place(x=50, y=20)
bt2 = Button(win, text="delete")
bt2.place(x=50, y=20)
bt1.pack()
bt1.grid(pady=50,padx=20)
bt2.pack()
bt2.grid(pady=70,padx=20)
win,mainloop()