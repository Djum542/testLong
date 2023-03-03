from tkinter import *

win = Tk()
win.geometry('400x400')
win.title('My info')

lb1 = Label(win, text="Ho ten sinh vien", font="Arial 16",bg="yellow")
lb1.grid(row = 0,column=1,ipadx=10,ipady=10)
lb2 = Label(win,text="MSSV",font="Arial 12")
lb2.grid(row=0,column=2)
lb3 = Label(win, text="Lop: K14PM01",font="Arial 12")
lb3.grid(row=1,column=2 , sticky=W)
lb3.place(x= 40, y= 50)
lb1.pack()
lb2.pack()
lb3.pack()
win.mainloop()