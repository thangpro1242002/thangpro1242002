import os
print("tất cả các tập tin và thư mục trong ổ C:")
link='C:\\Users\\DELL\\Documents'
print(os.listdir(link))
print("")

print("các thư mục:")
list1 = next(os.walk(link))[1]
print(list1)
print("")

print("các tệp:")
list2 = next(os.walk(link))[2]
print(list2)