import random
import string
# Nhập dung lượng dữ liệu giới hạn là  1MB <= size <= 1024MB.
dulieu=int(input('nhập giới hạn dữ liệu(MB)= '))
while (dulieu<1 or dulieu>1024):
	dulieu = int(input('nhập lại giới hạn dữ liệu (1->1024MB)= '))
# Giới hạn dung lượng mỗi file là  1000KB.
k=1000*1024
a= dulieu*(2**20)//(k)
b= dulieu*(2**20)%(k)
# Hãy sinh dữ liệu ngẫu nhiên kiểu chuỗi và lưu vào file
f= string.ascii_lowercase*48733
def text():
    c=''.join(random.sample(f,k))
    return c
print('số file có kích thước 1000KB là: ',a)
print('file cuối cùng có kích thước: ',b/1024,"KB")
for i in range(a):
	file=open('faker'+str(i+1)+'.txt' ,'x')
	file.write(text())
	file.close()
if b>0:
    file=open('cuvee'+'.txt' ,'x')
    file.write(''.join(random.sample(f,b)))
file.close()
print('Kxong bai')