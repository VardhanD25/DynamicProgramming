#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution(object):
    def maxProfit(self, prices,fee):
        n = len(prices)
        dp = [[0, 0] for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(2):
                if j==1:
                    dp[i][j]=max(-prices[i]+dp[i+1][0],dp[i+1][1])
                else:
                    dp[i][j]=max(prices[i]-fee+dp[i+1][1],dp[i+1][0])
        return dp[0][1]
