
N,K=map(int,input().split())

coins=sorted([int(input()) for _ in range(N) ],reverse=True)
cnt=0

for c in coins:
    if c<=K:
        n=K//c
        K=K%c

        cnt+=n
    if K==0:
        break
print(cnt)
