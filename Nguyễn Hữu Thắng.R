'C�u 1:
a)	12
b)	22
c)	600 '
'C�u 2:'
#1 (c): 
answer <- 10
answer <- prod(3:5) * answer
'C�u 3:'
#C1:
answer <- 0
for (j in 1:100){ answer <- j+answer }
#C2:
answer <- sum(1:100)
'C�u 4:'
#C1:
answer <- 1
for (j in 1:50){ answer <- j*answer }
#C2:
answer <- 1
answer <- prod(1:50)
'C�u 5:'
r <- 3:20
volume <- (4/3)*(r**3)
conversion <- data.frame(r=r, volume=volume)
print(conversion)
'C�u 6:'
index <- sapply(conversion,is.factor)
index
     
