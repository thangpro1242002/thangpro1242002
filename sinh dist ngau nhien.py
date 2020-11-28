import random
import string
alphago=dict()
n=random.randint(3,9)
g=random.choice(string.ascii_uppercase)
go=g+''.join(random.choice(string.ascii_lowercase) for _ in range(n-1))
alphago['name']=go
goo=random.randint(2,86)
alphago['age']=goo
print(alphago)


