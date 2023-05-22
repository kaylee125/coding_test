import sys

sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/baekjoon/input.txt', "r")
n=int(input())
stack=[]
for _ in range(n):
    
    num=int(input())
    if num !=0:
        stack.append(num)
    else:
        if stack:
            stack.pop()
        
            
        
print(sum(stack))