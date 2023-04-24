#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys
class Solution:
    def maxProfit(self, prices) :
        profit=0
        min_price=sys.maxsize
        #매 거래기회마다 최소금액을 구하고 그에대한 profit의 최대값을 산출
        for price in prices:
             min_price=min(min_price,price)
            profit=max(profit,price-min_price)
        return profit
    
solution=Solution()           
prices=[7,1,5,3,6,4]
print(solution.maxProfit(prices))