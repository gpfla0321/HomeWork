num_list = [1, 2, 3, 4, 5]
list_comprehension = []

for num in num_list:
    num = num ** 2
    list_comprehension.append(num)
    
print(list_comprehension)