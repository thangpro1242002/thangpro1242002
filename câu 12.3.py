import random
import string
#Tạo ngẫu nhiên số phần tử ditionary có trong list
n=random.randint(50,100)
print('Số phần tử trong list 1:',n)
faker=list()
for i in range(n):
    # Tạo giá trị ngẫu nhiên cho name: (chữ cái đầu tiên in hoa)
    z=random.randint(2,6)
    doinb = dict()
    huni=random.choice(string.ascii_uppercase)
    h = huni + ''.join(random.choice(string.ascii_lowercase) for i in range(z))
    doinb['name'] = h
    w = random.randint(1, 100) ##Tạo giá trị ngẫu nhiên cho age
    doinb['age'] = w
    faker.append(doinb) #Thêm phần tử dictionary vừa tạo vào list
print("list 2= ",faker)