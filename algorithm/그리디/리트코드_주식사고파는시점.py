#리스트의 i+1>i일 경우 주식을 팔아서 이익을 발생시킴

def maxprofit(price):
    profit=0
    for i in range(len(price)-1):
        if price[i+1]>price[i]:
            profit+=(price[i+1]-price[i])
    return profit
    


print(maxprofit([7,1,5,3,6,4]))