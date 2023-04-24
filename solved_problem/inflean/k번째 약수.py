import sys
sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/inflean/input.txt','r')

n,k=map(int,input().split())
a=[]

for i in range(1,n+1):
    if n%i==0:
        a.append(i)
#k번째 약수 구하기
if len(n)<k: 
    #N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 -1을 출력
    return -1
return a[k-1]