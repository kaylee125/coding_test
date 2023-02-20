'''
아이디어
-씨름선수 키,몸무게를 튜플로 받은 후  키 기준으로 내림차순 정렬하고 몸무게를 순차적으로 비교한다.

'''
import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'6. 씨름선수/in2.txt', "r")

n=int(input())
a=[]
for _ in range(n):
    t,w=map(int,input().split())
    a.append((t,w))

a.sort(reverse=True) #첫번째 인덱스 기준으로 내림차순 정렬  
cnt=0
max_weight=0
for t,w in a:
    if w>max_weight:
        cnt+=1
        max_weight=w
print(cnt)
    

