import sys

def dp(n):
    arr=[0]*1000001
    arr[1]=1
    arr[2]=2
    for s in range(3,n+1):
        #값이 너무 커서 int범위를 초과하기 때문에 배열에 넣을 값을 15746로 나누어줘야함
        arr[s]=(arr[s-1]+arr[s-2])%15746
    return arr[n]
print(dp(int(sys.stdin.readline())))