#https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution(object):
    def findNumberOfLIS(self, nums):
        n=len(nums)
        dp=[1]*n
        counts=[1]*n

        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    if dp[j]+1>dp[i]:
                        counts[i]=counts[j]
                        dp[i]=1+dp[j]
                    elif dp[j]+1==dp[i]:
                        counts[i]+=counts[j]
        ans=0
        maxi=max(dp)
        for i in range(n):
            if dp[i]==maxi:
                ans+=counts[i]
        return ans
        