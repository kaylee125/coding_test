def solution(number, k):
    answer = ''
    max=0
    for i in number:
        if max<int(i):
            max=int(i)
        answer+=str(max)

        if len(answer)==k:
            return answer

    
    # return answer
print(solution("1924",2))