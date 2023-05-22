import sys
sys.stdin=open('baekjoon/input.txt','r')
stack=[]

while True:
    s=input()
    if s=='.':
        break
    res=True #괄호가 하나도 없을때도 yes를 반환해야함.
    for x in s:
        if x=='(':
            stack.append('(')
        if x=='[':
            stack.append('[')
        if x==')' :
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                res=False
                break
        if  x==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                res=False
                break  
    if len(stack)==0 and res==True:
        print('yes')
    else:
        print('no')
    stack=[]

