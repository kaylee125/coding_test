import sys
sys.stdin=open('input.txt','r')

K=int(sys.stdin.readline().rstrip())

stack=[]
for _ in range(K):
    num =int(sys.stdin.readline().rstrip())
    if num==0 and stack:
        stack.pop()
    elif num !=0:
        stack.append(num)

if stack:
    print(sum(stack))
else:
    print(0)
 
    
        
        