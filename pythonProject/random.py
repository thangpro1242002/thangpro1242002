import pandas as pd
file = pd.read_csv("danh-sach-sinh-vien - Trang tính1.csv")
sinhvien = file.sample(7)
sinhvien.to_csv('7sinhvienngaunhien.csv',index=False)









