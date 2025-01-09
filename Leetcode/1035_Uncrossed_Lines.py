#https://leetcode.com/problems/uncrossed-lines/

class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        prev=[0]*(n+1)
        curr=[0]*(n+1)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(curr[j-1],prev[j])
            prev=curr[:]
        return prev[n]
