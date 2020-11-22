a=[0, 1, 2.5, 3, 4, 5, 6, 7, 8.5, 9, 10]
n=1
import math
for b in a:
    print(" giá trị phần tử thứ ",n, "=", b)
    n+=1
    if b>0:
        print("logarit tự nhiên phần tử thứ ",n, "=", math.log(b))
    else:
        print("Không có logarit phần tử thứ n")
    



