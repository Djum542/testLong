from tkinter import *
from tkinter import Menu

window = Tk()
window.title("Welcome to VniTeach app")

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
#Thực hiện hàm clicked khi người dùng chọn New
# new_item.add_command(label='New', command=clicked)
window.mainloop()