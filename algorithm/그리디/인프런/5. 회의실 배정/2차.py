import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'5. 회의실 배정/in3.txt', "r")

n=int(input())
meetings=[]
for _ in range(n):
    s,e=map(int,input().split())
    meetings.append((s,e))
    
meetings.sort(key=lambda x:(x[1],x[0])) 
cnt=1#첫번째 회의는 무조건 회의실 사용
ep=meetings[0]#첫번째 회의가 끝나는 시간
for i in range(len(meetings)):
    if ep[1]<=meetings[i][0]:
        cnt+=1
        ep=meetings[i]
print(cnt)
