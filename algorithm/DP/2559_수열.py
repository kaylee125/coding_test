n,k= map(int,input().split())
nums=list(map(int,input().split()))

prefix=[0]*(n+1)

for i in range(n):
    prefix[i+1]=prefix[i]+nums[i]

max=-200
for i in range(k,n+1):
    current=prefix[i]-prefix[i-k]
    if current>max:
        max=current
print(max)

"""
시간초과
max=-200
for i in range(n-k):
    current=0
    for j in range(i,i+k):
        current+=nums[j]
    if current>max:
        max=current
    
print(max)

"""


