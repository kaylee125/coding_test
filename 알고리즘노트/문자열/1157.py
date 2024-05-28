"""
문제설명: 가장 많은 빈도의 철자를 대문자로 출력
핵심내용: 알파벳 별 빈도수를 어떻게 count할것인지.
시간복잡도: O(N)
"""

word= input()
word=word.upper()
set_word=set(word)
dic_word={w:0 for w in set_word} #고유한 문자에 대해 딕셔너리 생성 후 value는 0으로 초기화

#철자별 갯수 세기
for s in word:
    if s in dic_word:
        dic_word[s]+=1
        
#가장 많은 철자 출력할때 for문으로 확인
max_value=[k for k,v in dic_word.items() if max(dic_word.values())==v]

if len(max_value)>1:
    print('?')
else:
    print(max_value[0])
