#https://leetcode.com/problems/longest-string-chain/

class Solution(object):
    def longestStrChain(self, words):
        n=len(words)
        dp=[1]*n
        words.sort(key=len)
        print(words)
        def compare(str1,str2):
            n1=len(str1)
            n2=len(str2)
            if n1!=n2+1:
                return False
            i=0
            j=0
            while(i<n1 and j<n2):
                if str1[i]==str2[j]:
                    j+=1
                i+=1
            return j==n2
        maxi=float("-inf")
        for i in range(n):
            for j in range(0,i):
                if compare(words[i],words[j]) and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
            maxi=max(maxi,dp[i])
        return maxi
        