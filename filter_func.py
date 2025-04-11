num_list = [10, 20, 30, 40, 50]
filter_list =[]

def filter(num_list):
    for num in num_list:
        
        if num > 30:  
            filter_list.append(num)
    return num_list  

filter(num_list)
print(filter_list)