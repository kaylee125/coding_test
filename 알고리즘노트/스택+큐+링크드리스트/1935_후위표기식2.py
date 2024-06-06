"""
후위표기법이란? : 연산자를 피연산자 뒤에 쓰는 연산표기법
문제설명:주어진 식을 후위표기법으로 계산한 결과를 소숫점 둘째자리까지 출력
핵심내용: 
    1) 후위표기법 계산 방식 이해
    2) 알파벳에 할당된 숫자가 무엇인지 이해

"""
import sys
sys.stdin=open('input.txt','r')
N=int(sys.stdin.readline())
cmd=sys.stdin.readline().rstrip()

num_list={x:int(sys.stdin.readline().rstrip()) for x in sorted(set(cmd)) if x.isalpha()}


nums={}
stack=[]
res=0
for w in cmd:
    
    #만약 알파벳이면
    if w.isalpha():
        stack.append(num_list[w])
    
    else:   
        n1=stack.pop()
        n2=stack.pop()
        if w=='+':
            stack.append(n2+n1)
            
        if w=='-':
            stack.append(n2-n1)
        if w=='*':
            stack.append(n2*n1)
        if w=='/':
            stack.append(n2/n1)
            
            
# print(round(float(stack[-1]),2)) 
print(f"{stack[-1]:.2f}") #소숫점 둘째자리까지 포멧팅하는 방법!!!

        
           
    
    
    
    
    
    
