N=int(input())
card_price=list(map(int,input().split())) #카드팩 가격 리스트


max_price=[0]*(N+1) # max_price[i]=카드 i개를 구매하는데 지불하는 최대금액

for i in range(1,N+1):
    for k in range(1,i+1):
        max_price[i]=max(max_price[i],max_price[i-k]+card_price[k-1])

print(max_price[N])
        