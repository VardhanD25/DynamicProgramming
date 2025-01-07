#https://leetcode.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins for amount 0
        
        # Iterate over each coin
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        # If dp[amount] is still inf, return -1
        return dp[amount] if dp[amount] != float('inf') else -1
                
        