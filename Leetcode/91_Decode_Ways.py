#https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0  
        dp = [-1] * n  

        def recur(ind):
            if ind == n:
                return 1
            if dp[ind] != -1:
                return dp[ind]
            jump1 = 0
            if s[ind] != '0':  
                jump1 = recur(ind + 1)
            jump2 = 0
            if ind < n - 1 and 10 <= int(s[ind:ind + 2]) <= 26:
                jump2 = recur(ind + 2)
            dp[ind] = jump1 + jump2
            return dp[ind]

        return recur(0)
