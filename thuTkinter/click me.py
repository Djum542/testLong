# from tkinter import *
#
# window = Tk()
# window.title("Welcome to VniTeach app")
# window.geometry('350x200')
# lbl = Label(window, text="Hello")
# lbl.grid(column=0, row=0)
#
# #Hàm khi nút được nhấn
# def clicked():
#     lbl.configure(text="Button was clicked !!")
#
# #Gọi hàm clicked khi nút được nhấn
# btn = Button(window, text="Click Me", command=clicked,background="yellow")
#
# btn.grid(column=1, row=1)
#
# window.mainloop()

# Cach 2
# from tkinter import *
#
# window = Tk()
# window.title("Welcome to VniTeach app")
# window.geometry('350x200')
# lbl = Label(window, text="Hello")
# lbl.grid(column=0, row=0)

#Hàm khi nút được nhấn
# def clicked():
#     lbl.configure(text="Button was clicked !!")
#
# #Gọi hàm clicked khi nút được nhấn
# btn = Button(window, text="Click Me", command=clicked)
# btn.grid(column=1, row=0)
#
# window.mainloop()

# Cach 3
# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("200x200")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()