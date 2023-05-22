import sys

sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/baekjoon/input.txt', "r")
n=int(input())

for _ in range(n):
    s=input()
    stack=[]
    for x in s:
        if x=='(':
            stack.append(x)
        elif x==')': 
            if stack :
                stack.pop()
            else:
                print('NO')
                break
    else:# break문으로 끊기지 않고 수행됬을경우 수행한다
        if not stack:
            print('YES')
        else:
            print('NO')
    
                