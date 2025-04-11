s = 'Python is awesome'
s = s.replace(" ", "")
s_low_list = s.lower()
cnt = 0

for s_low in s_low_list:
    if s_low in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1

print(f'모음 개수: {cnt}')
