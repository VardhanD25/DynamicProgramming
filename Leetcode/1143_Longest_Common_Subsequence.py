#https://leetcode.com/problems/longest-common-subsequence/

#Tabulation
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        len1=len(text1)
        len2=len(text2)
        dp=[[0]*(len2+1) for _ in range(len1+1)]

        
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len1][len2]

#Memoization
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        len1=len(text1)
        len2=len(text2)
        dp=[[-1]*len2 for _ in range(len1)]

        def recur(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if text1[ind1]==text2[ind2]:
                dp[ind1][ind2]=1+recur(ind1-1,ind2-1)
            else:
                dp[ind1][ind2]=max(recur(ind1-1,ind2),recur(ind1,ind2-1))
            return dp[ind1][ind2]
        return recur(len1-1,len2-1)
        
        