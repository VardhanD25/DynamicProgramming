#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[[0, 0, 0] for _ in range(2)] for _ in range(n + 1)]
        next1=[[0]*3 for _ in range(2)]
        curr=[[0]*3 for _ in range(2)]

        # Traverse in reverse order
        for index in range(n - 1, -1, -1):
            for buy in range(2):
                for rem in range(3):
                    if rem == 0 and buy==1:  # No transactions left
                        curr[buy][rem] = 0
                    elif buy == 1:  # Can buy
                        curr[buy][rem] = max(-prices[index] + next1[0][rem - 1], next1[1][rem])
                    else:  # Can sell
                        curr[buy][rem] = max(prices[index] + next1[1][rem], next1[0][rem])
                next1=curr[:]
        return next1[1][2]  # Return the maximum profit from index 0, buy allowed, and 2 transactions left
