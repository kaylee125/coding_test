def solution(n, words):
    answer = [0,0]#번호,차례
    word_list=[]
    cnt=0

    for i in range(1,len(words)):
        
        #한글자인 단어 or 이전에 등장했던 단어
        if words[i] in word_list or len(words[i])==1 or words[i-1][-1]!=words[i][0]:
            return answer 
        

        else:
            word_list.append(words[i])

    


       
        

    return 

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	))