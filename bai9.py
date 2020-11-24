import os
import time
n = "no"
while n == "no":
    n = input("Do you want to Shutdown? (nhập yes hoặc no)")
    if n =="no" :
         time.sleep(30)
    else:
        os.system('shutdown -s')