#스택으로 풀어보기


def solution(dartResult):
    stack=[]
    total=0

    dartResult=dartResult.replace("10","A")

    for s in dartResult:
        if s.isdecimal() or s=='A':
            if s=='A':
                stack.append(10)
            else:
                stack.append(int(s))
        if s=='D':
            val=stack.pop()**2
            stack.append(val)
        if s=='T':
            val=stack.pop()**3
            stack.append(val)
        if s=='*':
            val1=stack.pop()*2
            if len(stack):
                stack[-1]*=2    
            stack.append(val1)
        if s=='#':
            val=stack.pop()*(-1)
            stack.append(val)
    
    total=sum(stack)
    
    return total

print(solution(	'1S2D*3T'))
# print(solution('1D2S#10S'))
