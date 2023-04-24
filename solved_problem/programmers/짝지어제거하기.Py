def solution(s):
    answer = -1

    stack=[]
    s=list(s)

    
    for i in range(len(s)):
            
        if stack:
            if s[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

        else:
            stack.append(s[i])

    if stack:
        return 0
    else:
        return 1


print(solution('baabaa'))
print(solution('cdcd'))