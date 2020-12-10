import random
import string
n=random.randint(50,100)
ks=list()
i=1
for i in range(n):
    m=random.randint(2,6)
    doinb = dict()
    g = random.choice(string.ascii_uppercase)
    go = g + ''.join(random.choice(string.ascii_lowercase) for _ in range(m - 1))
    doinb['name'] = go
    goo = random.randint(1, 100)
    doinb['age'] = goo
    ks.append(doinb)
print(ks)
