def solution(n, words):
    answer = [0,0]#번호,차례
    #끝말잇기 단어 리스트
    done_words=[]
    for x in words:
        if x in done_words:
            return answer

        done_words.append(x)
        answer[1]+=1

        if len(x)==1 or x[0]==done_words[-1][0]:            
           return answer

        
        
        #탈락인 경우 1.이전에 등장한 단어일 경우 or 단어의 길이가 한글자인 경우 or 앞사람이 말한 단어의 마지막 문자로 시작하는 단어인 경우
       
        

    return words[-1][0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	))