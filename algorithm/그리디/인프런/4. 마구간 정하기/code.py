import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'4. 마구간 정하기/in1.txt', "r")

#mid의 길이로 몇마리의 말을 배치할 수 있는지
def Count(len):
    cnt=1
    endpoint=line[0] #첫번째말은 1번째에 배치
    for i in range(1,n):
            #현재좌표-마지막 말이 배치된 좌표가 len보다 크면 i번째 좌표에 말 배치가능
        if line[i]-endpoint>=len:
            cnt+=1
            endpoint=line[i]
        
n,c=map(int,input().split())
line=[]
for _ in range(n):
    line.append(int(input()))
res=0
line.sort()
lt=1 #최소거리
rt=line[n-1] #최대거리:마구간의 맨 끝 좌표

while lt>=rt:
    mid=(lt+rt)//2 #두 말 사이의 거리
    if Count(mid)>=c: 
        res=mid
        #더 넓은 거리에서도 위 조건이 성립하는지 확인해야함
        lt=mid+1
    else:#가장 인접한 거리가 너무 길기 때문에 mid 값을 좁혀야한다.
        rt=mid-1
