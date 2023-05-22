import sys
sys.stdin=open('baekjoon/input.txt','r')

arr=[]
max_len=0
ans=''
for i in range(5):
    row=list(map(str,input().split()))
    if max_len<len(row[0]):
        max_len=len(row[0])
    arr.append(row)
print(arr)
for j in range(max_len):
    for i in range(5):
        for k in range(max_len):
            try:
                ans+=arr[i][j][k]
                # print(ans)
            except:
                pass
print(ans)