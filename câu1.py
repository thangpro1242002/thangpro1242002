"""n = int(input("Nhập n: "))
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print("Tổng các số từ 1 tới", n, "là", s)"""
#Chuyển từ while -> for
n = int(input("Nhập n: "))
s = 0
for i in range(1, n+1):
    s += i
print("Tổng các số từ 1 tới", n, "là", s)