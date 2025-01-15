#https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution(object):
    def minCut(self, s):
        n = len(s)
        if n == 1:
            return 0
        
        dp = [-1] * n
        palindrome = [[False] * n for _ in range(n)]  # DP table for palindromes

        # Fill the palindrome table
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    palindrome[i][j] = True
                elif length == 2:
                    palindrome[i][j] = (s[i] == s[j])
                else:
                    palindrome[i][j] = (s[i] == s[j]) and palindrome[i + 1][j - 1]

        # Now use this table to compute the min cuts
        def recur(ind):
            if ind == n:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            mini = float('inf')
            for j in range(ind, n):
                if palindrome[ind][j]:
                    cost = 1 + recur(j + 1)
                    mini = min(mini, cost)
            dp[ind] = mini
            return mini

        return recur(0) - 1