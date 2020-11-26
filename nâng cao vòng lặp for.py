list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}),
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}),
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}),
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for index, (x,y) in enumerate(list2):
    #khi phân tích ra thì x, y là các dictionary
    for i in x: #i chạy trong x nhận các giá trị lần lượt là: 'name', 'age'
        print(x[i],end=' ')
    print(' ')
    for i in y: #i chạy trong y nhận các giá trị lần lượt là: 'name', 'age'
        print(y[i],end=' ')
    print(' ')