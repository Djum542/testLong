# from tkinter import *
# from tkinter import scrolledtext
# win = Tk()
# win.title("Welcome to app")
# win.geometry("300x200")
# txt = scrolledtext.ScrolledText(win,width="40",height="50")
# txt.grid(column=0,row=0)
# win.mainloop()
from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Welcome to VniTeach app")
window.geometry('350x200')

txt = scrolledtext.ScrolledText(window,width=40,height=10,)
txt.grid(column=0,row=0)
txt["state"] = "disable"
window.mainloop()