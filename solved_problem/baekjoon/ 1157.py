word= input()
word=word.upper()
set_word=set(word)
dic_word={alphabet:0 for alphabet in set_word}

#철자별 갯수 세기
for s in word:
    if s in dic_word:
        dic_word[s]+=1
#가장 많은 철자 출력하기
max_value=[k for k,v in dic_word.items() if max(dic_word.values())==v]

if len(max_value)>1:
    print('?')
else:
    print(max_value[0])
