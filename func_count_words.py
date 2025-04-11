s = str(input('문자열을 입력하세요: '))

def count_words(st):
    w = st.split()
    return len(w)

print(count_words(s))