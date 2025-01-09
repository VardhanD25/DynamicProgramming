#https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution(object):
    def minInsertions(self, s):
        n=len(s)
        prev=[0]*(n+1)
        curr=[0]*(n+1)
        str1=s[:]
        str2=s[::-1]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(curr[j-1],prev[j])
            prev=curr[:]
        return n-prev[n]
        