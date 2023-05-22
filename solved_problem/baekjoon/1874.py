import sys
sys.stdin=open('baekjoon/input.txt','r')
n=int(input())
stack=[]
arr=[int(input()) for _ in range(n)]
ans=[]
for i in range(1,n+1):
    stack.append(i) #append하는 경우 
    ans.append('+')
    #arr의 첫번째 글자와 i와 동일할때까지 append하다가 동일하면 pop한다.
    while arr and stack:
        if arr[0]==stack[-1] and stack:   
            ans.append('-')
            stack.pop()
            del(arr[0])
        else:break
if stack:
    print('NO')
else:
    for x in ans:
        print(x)
