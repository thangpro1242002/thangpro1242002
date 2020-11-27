import  random
n=random.randrange(50,1000)
print(n)
#apple=list()
#for i in range(n):
    #apple.append(input('nhap phan tu'))
#print(apple)
print('ket thuc cau 1')
apple1=list()
for i in range(n):
    apple1.append(random.randrange(-1000,1000))
print(apple1)
print('ket thuc cau 2')
apple2=list()
for i in range(n):
    apple2.append(random.triangular(-1000.0,1000.0))
print(apple2)
print('ket thuc cau 3')