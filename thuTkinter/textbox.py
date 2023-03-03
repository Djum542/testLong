from tkinter import *

window = Tk()
window.title("Welcome to VniTeach app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

#Tạo một Textbox
txt = Entry(window,width=10)
#Vị trí xuất hiện của Textbox
txt.grid(column=1, row=0)

#Đặt vị trí con trỏ tại Textbox
txt.focus()

#Hàm xử lý khi nút được nhấn
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

#Để tắt chức năng nhập của Textbox bằng state
txt = Entry(window,width=10, state='disabled')
txt.place(x= 25, y=100)
textbox = Text(window, fg="blue")
textbox.place(x=25, y=60)
def data():
    str = "hinh nhu"
    textbox.insert(1.0, str)
    textbox.insert(END, "123456")
window.mainloop()