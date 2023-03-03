from tkinter import  *
from tkinter import messagebox
from tkinter.ttk import Combobox

# thiet lapj cac gia tri va thuoc tinhs cho khung nen
win = Tk()
win.geometry('400x400')
win.title("Graphic User Interface")
# thiet lap cac nhan va vi tri cua chung trong persons
name = Label(win, text="Ho va ten", font="arial 16")
number = Label(win, text="200811009", font= "Arial 16 ", background="blue")
student = Label(win, text="k14", font="Arial 16", bitmap="", background="blue")
# bitmap: hien thi hinh anh
# border: kich thuoc duong vien bao quanh nhan
# cursor: thiet lap loai con tro chuot.
# foreground: mau cua van ban trong nhan hoac bitmap
# height: dat do cao cua nhan
# image: hien thi anh tinh
#ipadx || ipady: khoang cach phia trong. 
# justify: quy dinh nhieu dong van ban can le trai, giua, phai.
# padx: xac dinh khoang chong truoc hoac sau chu.
# pady: xac dinh khoang trong tren va duoi.
# relief: chi dinh su xuat hien cua duong vien.
# wraplength: dat do dai cho dong trong nhan
func = Label(win, cursor="",wraplength="", foreground="red", text="nhan dan", padx="",pady="",justify="", height="20", image="")
name.pack()
number.pack()
student.pack()
func.pack()
# Lam viec voi button
b1 = Button(win,foreground="", activebackground="", border="",background="",command="")
# activebackground: mau cua nut button khi con tro o tren nut.
# activeforeground: mau chu cua nut khi con tro chuot o tren.
# border: duong vien nut.
# background: mau nen cho nut.
# command: Ham hoac phuong thuc se duoc goi khi nhan
# foreground: mau cho chu
# highlightcolor: thay doi mau khi nut co tam diem
# image:
# height:
# padx
# pady:
# relief: value(sunken, raised,groove,ridge)
# state: de chuyen nut sang vo hieu hoa mau xam.
# wraplength: do dai cua chu
name.configure(win,text="nut thay doi")
win.mainloop()
# flash: chuyen doi mau tu dong giua hai mau.
# invoke:   goi lai nut va tra ve ham do da tra ve(sau ra ket qua sau an nut luon maf chua can click).

# entry: tao ra o textbox de nhap vao
txt = Entry(win,width="20")
txt.grid(column=1,row=0)
# focus: vi tri con tro tai textbox

#Tạo hộp chọn Combobox
combo = Combobox(win)
#Các giá trị của hộp chọn
combo['values']= (1, 2, 3, 4, 5, "Text")
#Thiết lập giá trị được chọn
combo.current(1) #set the selected item
#Thiết lập trạng thái của Checkbox
chk_state = BooleanVar()
chk_state.set(True) #set check state
#Tạo Checkbox có trạng thái đã tích chọn
chk = Checkbutton(win, text='Choose', var=chk_state)
# nut radio
rad1 = Radiobutton(win,text='First', value=1, variable=selected)
#Hộp thoại báo lỗi
messagebox.showerror('Message title', 'Message content')
# hop thoai cau hoi
res = messagebox.askquestion('Message title','Message content')
res = messagebox.askyesno('Message title','Message content')
res = messagebox.askyesnocancel('Message title','Message content')
res = messagebox.askokcancel('Message title','Message content')
res = messagebox.askretrycancel('Message title','Message content')
#Tạo spinbox có chiều rộng 5, giá trị từ 0 đến 100
spin = Spinbox(win, from_=-10, to=100, width=5)
#lam viec voi menu
menu = Menu(win)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
win.config(menu=menu)
