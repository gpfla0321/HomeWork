from datetime import datetime

s = '901212-1234567'
s_s = s.split('-')
birth = s_s[0]
year = birth[:2]
month = birth[2:4]
day = birth[4:6]
todayYear = str(datetime.today().year)

if int(year) > int(todayYear[2:4]):
    year = '19'+ year
    
print(f'{year}년 {month}월 {day}일')