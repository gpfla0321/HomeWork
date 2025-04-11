email = input('이메일을 입력하세요: ')
email_cnt_a = email.count('@')
email_cnt_s = email.count('.')

print(f'이메일 주소: {email}')
if email_cnt_a == 1:
    if email_cnt_s <= 0:
        print('유효하지 않음')
    else:
        print('유효함')
else:
    print('유효하지 않음')