import numpy as np
_A=[[2,3,4],[123,456,789],[159,357,468]]
A=np.array(_A)
print(A)
_B=([3,2,9],[178,239,472],[245,672,234])
B=np.array(_B)
print(B)
print('A+B=\n', A+B)
print('A*B=\n', A.dot(B))
print('ma tran chuyen vi cua A:\n',np.transpose(A))
print('ket thuc bai 1')
import pandas as pd
df= pd.read_csv("ahihi.csv")
print(df.head(12))
url="https://www.kaggle.com/sazid28/advertising.csv"
ok=pd.read_csv(url)
print(ok.head(12))
url1='https://api.exchangerate-api.com/v4/latest/usd'
aaa=pd.read_json(url1)
print(aaa.head(12))
print('ket thuc bai 2')
#cot
import matplotlib.pyplot as plt
cot=['faker','cuvee','ambition','chovy','crown']
dong=[238,478,369,234,457,78]
plt.bar(cot,dong,color='red')
plt.title("huni")
plt.xlabel("peanut")
plt.ylabel("bang")
plt.show()
#cot ghep
cot=['faker','cuvee','ambition','chovy','crown']
dong1=[12,17,23,7,9]
dong2=[2,4,9,5,6]
index= np.arange(5)
width=0.30

plt.bar(index,dong1,width,color='green',label='wolf')
plt.bar(index+width,dong2,width,color='blue',label='soft')
plt.title('ruler')

plt.ylabel('ruler')
plt.xlabel('peanut')
plt.xticks(index+width/2,cot)
plt.legend(loc='best')
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