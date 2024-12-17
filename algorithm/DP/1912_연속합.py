n=int(input())
arr=list(map(int,input().split()))

max_prefix=[0]*len(arr)
max_prefix[0]=arr[0]

for i in range(1,len(arr)):
   choose=max(max_prefix[i-1]+arr[i],arr[i])
   max_prefix[i]=choose

print(max(max_prefix))