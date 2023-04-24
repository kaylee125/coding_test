

def solution(s):
    #숫자영단어 딕셔너리 생성
    num_dict={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    word=''
    answer=''
    for x in s:
        if x.isdecimal():
            answer+=x
        else:
            word+=x
            if word in num_dict.keys():
                answer+=str(num_dict.get(word))
                word=''
    return int(answer)
    
print(solution("123"))
# num_dict={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
# print(num_dict.get('zero'))