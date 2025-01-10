#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        
        mini=prices[0]
        profit=0
        for i in prices:
            cost=i-mini
            profit=max(profit,cost)
            mini=min(mini,i)
        return profit