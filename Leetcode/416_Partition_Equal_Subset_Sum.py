#https://leetcode.com/problems/partition-equal-subset-sum/

class Solution(object):
    def canPartition(self, nums):
        n=len(nums)
        if n==1:
            return False
        total=sum(nums)
        dp=[[False]*(2*total+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        dp[0][2*nums[0]]=True
        for index in range(1,n):
            for target in range(1,total+1):
                nottake=dp[index-1][target]
                take=False
                if 2*nums[index]<=target:
                    take=dp[index-1][target-2*nums[index]]
                dp[index][target]=take or nottake
        return dp[n-1][target]

#Further optimised approach
class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        # If total sum is odd, partition is not possible
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        
        # DP array to track achievable sums up to the target
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum of 0 is always achievable
        
        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] = dp[t] or dp[t - num]
        
        return dp[target]
