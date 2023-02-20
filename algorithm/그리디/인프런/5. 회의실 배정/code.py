import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'5. 회의실 배정/in1.txt', "r")

n=int(input())
meeting=[]
for x in range(n):
    s,e=map(int,input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x:(x[1],x[0]))

endtime=0 #끝나는 시간
cnt=0 #회의 갯수
for s,e in meeting:
    if s>=endtime:
        endtime=e
        cnt+=1
print(cnt)


