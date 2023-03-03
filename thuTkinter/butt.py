from tkinter import *

win = Tk()
win.geometry("200x180")


def click():
    Lb = Label(win, text="Button Function")
    Lb.place(x=70, y=50)


butt = Button(win, text="Function", activebackground='red', bg='yellow', fg='green', command=click)
butt.pack(side=RIGHT)


def close_ct():
    win.destroy()  # Hàm đóng chương trình


Lb2 = Label(win, text="Display: ")
Lb2.place(x=20, y=50)
butt.grid(pady=10, padx= 10)
butt1 = Button(win, text="Close", command=close_ct)  # Nút đóng chương trình
butt1.pack()
butt1.grid(pady=10, padx= 10)
win.mainloop()