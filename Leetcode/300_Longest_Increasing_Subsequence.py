#https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        n=len(nums)
        dp=[[0]*(n+1) for _ in range(n+1)]

        #Adjust prev by +1 because we cannot store -1 as index

        for ind in range(n-1,-1,-1):
            for prev in range(ind-1,-2,-1):
                nottake=dp[ind+1][prev+1]
                take=float('-inf')
                if prev==-1 or nums[ind]>nums[prev]:
                    take=1+dp[ind+1][ind+1]
                dp[ind][prev+1]=max(take,nottake)
        return dp[0][0]

#Another solution by tabulation (simplified approach)
class Solution(object):
    def lengthOfLIS(self, nums):
        n=len(nums)
        dp=[1]*n
        for i in range(n):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],1+dp[j])
        return max(dp)