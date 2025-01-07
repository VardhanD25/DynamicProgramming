#https://leetcode.com/problems/coin-change-ii/

class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: one way to make amount 0 (no coins)
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        
        return dp[amount]
