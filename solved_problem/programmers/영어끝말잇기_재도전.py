def solution(n, words):
    for i in range(1,len(words)):
        if len(words[i])==1:
            return -1
        #틀리는 조건
        #1.앞 단어의 끝 철자와 현재 단어의 첫번째 철자가 일치하지 않거나
        #2.기존에 나왔었던 단어가 또 나오는 경우 
        if words[i][0]!=words[i-1][-1] or words[i] in words[:i]:
            #탈락한 사람의 번호
            number=(i%n)+1
            #몇번째 차례에 탈락했는지
            order=int((i/n)+1)
            return [number,order]
            
    else:
        return [0,0]


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))