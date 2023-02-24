'''
주어진 배열 a와 1부터 n까지의 수를 담은 리스트를 비교할경우 
엑스자로 교차하지 않으려면 주어진 a배열이 증가하는 수열이여야한다.
a배열의 최대증가수열의 길이를 구하면 되므로 4번 최대부분증가수열과 코드가 동일하다.

'''

import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 8/'
sys.stdin=open(base+'5. 최대 선 연결하기/in1.txt', "r")

n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)#1번째 원소를 인덱스1에 위치시키기 위해 
dp=[0]*(n+1)
dp[1]=1

res=0

for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1):
        if a[j]<a[i] and max< dp[j]:
            max=dp[j]
    dp[i]=max+1
if res<dp[i]:
    res=dp[i]

print(res)