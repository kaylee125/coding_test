def solution(s):
    answer=0
    cnt=0

    while s:
        s0=s[0]
        for i in range(len(s)):
            if s[i]==s0:
                cnt+=1
            else:
                cnt-=1
            if cnt==0 or i==len(s)-1:
                answer+=1
                s=s[i+1:]
                break
    return answer
    
print(solution("banana"))