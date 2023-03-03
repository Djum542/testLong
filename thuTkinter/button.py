from tkinter import *
win = Tk()
win.geometry('200x300')
def click():
    lb = Label(win, text="unbox")
    lb.place(x= 50, y= 60)
def close():
    win.destroy()
lb = Label(win, text="Dislay:")
lb.place(x= 50, y= 30)
button = Button(win, text="Nhan vao", activebackground="red",bg='yellow')

button0 = Button(win, text="Exit")
button0.pack()
button.pack()
win.mainloop()
