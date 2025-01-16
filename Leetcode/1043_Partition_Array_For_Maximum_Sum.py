#https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        n=len(arr)
        dp=[0]*(n+1)

        for i in range(n-1,-1,-1):
            len1=0
            maxi=float('-inf')
            maxans=float('-inf')
            for j in range(i,min(i+k,n)):
                len1+=1
                maxi=max(maxi,arr[j])
                sum1=len1*maxi+dp[j+1]
                maxans=max(maxans,sum1)
            dp[i]=maxans
        return dp[0]

        