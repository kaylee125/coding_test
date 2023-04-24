#  #문자클래스 []:[]사이의 문자들과 매치
#  #dot(.):줄바꿈(\n)을 제외한 모든 문자와 매치
#  #반복(*): ca*t ->a가 0번부터 n번까지의 반복에 대해 매칭
#  #반복(+):ca+t->0번 반복되면 매칭되지 않음
#  #ca{2}t->a가 2번 반복될 경우에만 매칭
#  #ca{2,5}t:2~5번 반복될 경우만 매칭
#  #ab?c:?={0,1} 0또는 1회 반복에 대해서만 매칭

import re
p=re.compile('[a-z]+') #a부터 z까지 문자열 중 한번 이상 반복되는 것을 찾는 정규식

#match

m=p.match('python')
print(m)

#match객체:
    #group():매치된 문자열을 리턴
    #start():매치된 문자열의 시작 위치를 리턴
    #end():매치된 문자열의 끝 위치를 리턴
    #span():매치된 문자열의 (시작,끝)에 해당되는 튜플을 리턴
print(m.group())

#search
m=p.search('3 python')
print(m)

#findall:일치하는걸 찾아서 리스트로 리턴
m=p.search('3 python')
print(m)

#컴파일 옵션
#dotall:dot에서 줄바꿈 문자도 포함하도록 하는 
p=re.compile('a.b',re.DOTALL)
m=p.match('a\nb')
print(m)
#위 두 식 한번에 표현하기
print(re.match('a.b','a\nb'))
#ignorecase
p=re.compile('[a-z]',re.IGNORECASE)
print(p.match('Python'))

#multiline,M 여러줄
p=re.compile('^python\s\w+',re.MULTILINE) #^:python이 맨 처음 나와야함 /\s:공백 / \w:word(단어)

data="""python one
life is too short
python two
python three
you need python
"""
print(p.findall(data))

#r:로우스트링

#그루핑
