#https://leetcode.com/problems/word-break/

class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[n][i] = True
        
        
        for start in range(n - 1, -1, -1):  
            for ind in range(n-1,start-1,-1):  
                if s[start:ind + 1] in wordDict:  
                    dp[start][ind] = dp[ind + 1][ind + 1] or dp[start][ind + 1]
                else:  
                    dp[start][ind] = dp[start][ind + 1]
        return dp[0][0]