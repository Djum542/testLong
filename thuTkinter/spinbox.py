from tkinter import *

window = Tk()
window.title("Welcome to VniTeach app")
window.geometry('350x200')

# #Tạo spinbox có chiều rộng 5, giá trị từ 0 đến 100
# spin = Spinbox(window, from_=-10, to=100, width=5)
# spin.grid(column=0,row=0)
#spinbox chỉ gồm có 3 giá trị là 3, 5 và 10
# spin = Spinbox(window, values=(3, 5, 10), width=5)
# spin.grid(column=1,row=1)
# Dat gia tri mac dinh cho
var =IntVar()

#Đặt giá trị mặc định là 25
var.set(25)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin.grid(column=0,row=1)
window.mainloop()