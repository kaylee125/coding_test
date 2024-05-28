

text = "  Hel,lo, Pytho,n!  "

print('문자열 인덱싱')
# 문자열 특정위치에 있는 문자 추출
print(text[0])
print(text[-1])

print('문자열 슬라이싱')
#부분문자열 추출
print(text[:])
print(text[-1:-4])
print(text[2:])


print('특정 문자가 있는지 확인')
print('P' in text)

print('문자열이 같은지 비교')

print("Hello, Python!"==text)


print('문자열 길이 반환')
print(len(text))

print('특정 문자의 인덱스 값 찾기')
print(text.index('P'))

print('문자열을 구분자 기준으로 나누고 합치기')
# 나누기
print(text.split())
print(text.split(','))

#합치기
list=['a','p','p']
print(''.join(list))


print('문자열 대소문자 변환')
print(text.upper())
print(text.lower())


print('기존 값을 다른 값으로 치환')
print(text.replace(',','/'))

print('양쪽 끝에서 특정 문자(혹은 공백) 제거')
print(text.strip())
print(text.lstrip())
print(text.rstrip())

print('아스키코드로 변환 혹은 대소 비교')
print(ord('a')>ord('b'))
print(ord('a'),ord('b'))

## isalpha,isdigit,isalnum
print(text.isalnum())