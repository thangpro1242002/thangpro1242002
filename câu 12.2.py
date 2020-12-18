import random, string
faker=dict()
#Tạo giá trị cho name
n=random.randint(3,9)
huni=random.choice(string.ascii_uppercase)
doib=huni+''.join(random.choice(string.ascii_lowercase) for _ in range(n-1))
faker['name']=doib
#Tạo giá trị ngẫu nhiên cho age
bang=random.randint(1,120)
faker['age']=bang
print('Dictionary vừa tạo:',faker)
