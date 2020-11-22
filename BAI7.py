import random
n=int (input ("nhập n: "))
list_rd=[random.random ()
for i in range(n)]
print ("list_rd= ",list_rd)
MIN=list_rd [0]
for i in list_rd:
    if i < MIN:
        MIN = i
print ("MIN của list: ",MIN)