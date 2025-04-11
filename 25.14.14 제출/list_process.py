# 1. 리스트에 orange 추가
fruit_list = ["apple", "banana", "cherry"]
fruit_list.append('orange')
print(fruit_list)

# 2. [10, 20, 30]의 합
num_list = [10, 20, 30]
hap = 0

for num in num_list:
    hap += num

print(f'합계: {hap}')

# 3. [1, 2, 3, 4, 5] 역순 출력
rev_list = [1, 2, 3, 4, 5]
rev_list.reverse()

print(rev_list)

# 4. [5, 2, 8, 1, 9] 리스트를 오름차순으로 정렬하세요.
sort_list = [5, 2, 8, 1, 9]
sort_list.sort()
print(sort_list)