
from tkinter import *
import pandas as pd
data = {'Tên sản phẩm': ['Sản phẩm A', 'Sản phẩm B', 'Sản phẩm C', 'Sản phẩm D', 'Sản phẩm E'],
        'Giá tiền': [100, 200, 300, 400, 500],
        'Số lượng': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Tạo cửa sổ form
window = tk.Tk()

# Tạo bảng dữ liệu từ DataFrame
table = tk.Frame(window)
table.pack(side='top', padx=10, pady=10)
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        cell = tk.Label(table, text=df.iloc[i, j])
        cell.grid(row=i, column=j, padx=5, pady=5)

# Tạo nút đóng cửa sổ
button = tk.Button(window, text='Đóng', command=window.destroy)
button.pack(side='bottom', padx=10, pady=10)

# Hiển thị cửa sổ form
window.mainloop()
