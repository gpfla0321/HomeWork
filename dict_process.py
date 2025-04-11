# 1. {"name": "John", "age": 30} 딕셔너리에서 "age"의 값 출력
per_dic = {"name": "John", "age": 30}
print(f'나이: {per_dic['age']}')

#2. {"math": 90, "science": 85, "history": 78} 딕셔너리에서 모든 과목명을 출력하세요.
sub_dic = {"math": 90, "science": 85, "history": 78}
print(f'과목들: {list(sub_dic.keys())}')

#3. {'apple': 3, 'banana': 5}에서 apple의 값을 2 증가시키세요.
fruit_dic = {'apple': 3, 'banana': 5}
fruit_dic['apple'] += 2

print(fruit_dic)