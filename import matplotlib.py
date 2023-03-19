import matplotlib.pyplot as plt

sales_data = data['sales']
months = data['month']

plt.bar(months, sales_data)
plt.xlabel('Tháng')
plt.ylabel('Doanh số')
plt.title('Thống kê doanh số theo tháng')
plt.show()
