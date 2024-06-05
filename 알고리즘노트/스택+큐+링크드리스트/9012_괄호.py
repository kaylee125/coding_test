
"""
문제설명:
핵심내용:
시간복잡도: 스택은 O(1)
"""

N=int(input())

for _ in range(N):
    test=input()
    stack=[]
    
    for x in test:
        if x =='(':
            stack.append(x)
        else:
            if stack and stack[-1]=='(': #stack[-1]=='(' 조건은 삭제해도 무방함. stack에 데이터가 있다는건 '('값이 있다는 의미이기 때문에
                stack.pop()
                
            else:
                stack.append(x)
    if stack: #stack에 데이터가 있으면 짝이 안맞음 
        print('NO')
    else:
        print('YES')