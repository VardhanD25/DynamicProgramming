#https://leetcode.com/problems/longest-palindromic-subsequence/

#Great question
#This question is simply finding the longest common subsequence of the string and it's reverse
class Solution(object):
    def longestPalindromeSubseq(self, s):
        n=len(s)
        dp=[[0]*(n+1) for _ in range(n+1)]

        str1=""
        str2=""
        for i in range(n):
            str1+=s[i]
            str2+=s[n-i-1]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n][n]
        