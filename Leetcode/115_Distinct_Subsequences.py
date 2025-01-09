#https://leetcode.com/problems/distinct-subsequences/

class Solution(object):
    def numDistinct(self, str1, str2):
        n=len(str1)
        m=len(str2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][m]
    
#1D Space optimised

class Solution(object):
    def numDistinct(self, str1, str2):
        n=len(str1)
        m=len(str2)
        prev=[0]*(m+1)

        prev[0]=1
        for i in range(1,n+1):
            for j in range(m,0,-1):
                if str1[i-1]==str2[j-1]:
                    prev[j]=prev[j-1]+prev[j]
        return prev[m]
        