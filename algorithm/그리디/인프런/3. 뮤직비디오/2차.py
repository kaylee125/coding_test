'''
아이디어
-dvd의 최소용량크기 구하기
-n개의 곡을 m개의 dvd에 순서대로 넣어야함

자료구조
-int res ->dvd 최소용량 
-Count(res)

'''

import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'3. 뮤직비디오/in2.txt', "r")

n,m=map(int,input().split())
arr=list(map(int,input().split()))
res=0
lt=1
rt=sum(arr)
maxx=max(arr)

#해당 용량으로 노래를 몇개의 CD에 나누어 담을 수 있는지 확인
def Count(capacity):
    cnt=1
    sum=0
    for x in arr:
        if sum+x>=capacity: #sum(누적용량)+현재노래(x)를 더한 값이 capacity를 초과하는지 확인.
            #초과하면 다음 CD에 저장해야함
            cnt+=1
            sum=x #CD의 갯수를 늘려준 뒤, 누적용량을 현재 노래(x)로 다시 초기화
        else:
            sum+=x
    return cnt
        

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)<=m and mid>=maxx:#반례조건 추가:가장 용량이 큰 노래가 하나의 DVD용량보다는 크거나 같아야함
        res=mid
        #조건에 부합하는 더 작은 mid값이 존재하는지 확인해야함 ->작은 값들 중 확인
        rt=mid-1
    else:#용량이 작으므로 더 큰 쪽에서 확인해아함
        lt=mid+1
print(res)

