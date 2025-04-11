# minority_list = []

# x = int(input('시작 값: '))
# y = int(input('끝 값: '))

# def find_primes(x, y):
#     for num in range(x, y+1):
#         if num != 1:
#             for i in range(1, num+1):
#                 if i != 1 or i != num:
#                     if num % i == 0:
#                         minority_list.append(num)
                    
#     return minority_list

# print(find_primes(x, y))

# 강사님 이 부분은 잘 안돼서 AI의 도움을 받았습니다 윗 부분이 제가 하단 만 코드입니다.


def find_primes(x, y):
    minority_list = []
    for num in range(x, y + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            minority_list.append(num)
    return minority_list

x = int(input('시작 값: '))
y = int(input('끝 값: '))

print(find_primes(x, y))