import os

r_list = []

def calculator(x, y, o):
    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o =='*':
        return x * y
    elif o == '/':
        return x / y

r_list.append(calculator(1,1,'*'))
r_list.append(calculator(2,2,'*'))
r_list.append(calculator(3,3,'*'))
r_list.append(calculator(4,4,'*'))
r_list.append(calculator(5,5,'*'))

print(r_list)


#1)  두 수와 연산자(+, -, *, /)를 인자로 받아 계산하는 calculator 함수를 작성하세요

#    calculator() 함수를 선언
#    	def calculator(a, b, op):

#    결과: [1, 4, 9, 16, 25]