#https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution(object):
    def minDistance(self, word1, word2):
        n=len(word1)
        m=len(word2)
        prev=[0]*(m+1)
        curr=[0]*(m+1)
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(prev[j],curr[j-1])
            prev=curr[:]
        return m+n-(2*prev[m])
        