import random
n=int (input ("nhập n: "))
list_rd=[random.random ()
for i in range(n)]
print ("list_rd= ",list_rd)
MAX=list_rd [0]
MIN=list_rd [0]
for i in list_rd:
    if i >=MAX:
        MAX=i
print("MAX của list: ", MAX)