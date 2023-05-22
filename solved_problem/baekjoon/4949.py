import sys
sys.stdin=open('baekjoon/input.txt','r')
stack=[]
for s in sys.stdin:
    if s=='.':
        break
    for x in s:
        if x=='(':
            stack.append('(')
        if x=='[':
            stack.append('[')
        if stack and x==')' :
            if stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')
                break
        if stack and x==']':
            if stack[-1]=='[':
                stack.pop()
            else:
                stack.append(']')
                break  
    if stack:
        print('no')
    else:print('yes')
    stack=[]