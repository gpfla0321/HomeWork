kg = int(input('체중: '))
cm = int(input('키: '))

m = cm * 0.01
bmi = kg /(m ** 2)

print('체중(kg): ', kg)
print('키(m): ', cm)
print('BMI: ', bmi)