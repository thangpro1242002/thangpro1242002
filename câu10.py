#1. Numpy
import numpy as np
#Tạo ma trận
A = np.array([[3, 5, 7], [2, 4, 6], [12, 14, 16]])
B = np.array([[2, 4, 5], [7, 9, 11], [14, 16, 18]])
print(A + B)  #Tổng 2 ma trận
print(A.dot(B))  #Tích 2 ma trận
#Chuyển vị ma trận
print(A.transpose())
print(B.transpose())
#2. Pandas
import pandas as pd
df1= pd.read_csv("Canadaa.csv")
print(df1.head(10))
df2=pd.read_csv("https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2019-financial-year-provisional/Download-data/annual-enterprise-survey-2019-financial-year-provisional-csv.csv")
print(df2.head(10))
df3=pd.read_json('https://api.exchangerate-api.com/v4/latest/usd')
print(df3.head(10))
#3. Matplotlib
import numpy as np
import matplotlib.pyplot as plt
divisions = ["gà", "dê", "heo", "vịt","ếch"]
divisions_average_marks = [80,63,72,67,90]
plt.bar(divisions, divisions_average_marks, color = 'blue')
plt.title("Trung bình mỗi người ăn động vật trong 1 năm")
plt.xlabel("Tên động vật")
plt.ylabel("%")
plt.show()
 #- Đồ thị hình bar
import matplotlib.pyplot as plt
import numpy as np
divisions = ["máy bay", "ô tô", "xe máy", "trực thăng", "xe đạp"]
division_average_marks = [60,80,50,70,40]
boys_average_marks = [40,60,57,38,65]

index = np.arange(5)
width = 0.20

plt.bar(index, division_average_marks, width, color= 'green', label= 'Thái Lan')
plt.bar(index+ width, boys_average_marks, width, color = 'red', label= 'Việt Nam')
plt.ylabel("%")
plt.xlabel("Các loại phương tiện")
plt.xticks(index+ width/2, divisions)
plt.legend(loc = 'best')
plt.show()
#line
plt.plot([1,3,6,5],[1,5,4,5],linestyle='-.')
plt.title('line')
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()
#box plot
import random
x = np.random.randn(100) + np.arange(0, 100) * 0.5
y = np.random.randn(100) + np.arange(0, 100) * 1.0 + 10
z = np.random.randn(100) + np.arange(0, 100) * 2 - 15

plt.boxplot([x, y, z],
            labels = ['x', 'y', 'z'],
            showfliers = True)
plt.title('Biểu đồ Boxplot')
plt.xlabel('Classes')
plt.ylabel('Gía trị của x, y, z')
plt.show()