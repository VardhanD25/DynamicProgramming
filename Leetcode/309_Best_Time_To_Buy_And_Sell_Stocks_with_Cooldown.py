#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        dp=[[0]*3 for _ in range(n+1)]
        next1=[0]*3
        curr=[0]*3

        for index in range(n-1,-1,-1):
            for buy in range(3):
                if buy==2:
                    curr[buy]=next1[1]
                elif buy==1:
                    curr[buy]=max(-prices[index]+next1[0],next1[1])
                else:
                    curr[buy]=max(prices[index]+next1[2],next1[0])
            next1=curr[:]
        return next1[1]
        

        