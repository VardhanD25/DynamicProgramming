#https://leetcode.com/problems/house-robber/
class Solution(object):
    def rob(self, nums):
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp=[0]*n #stores max money you can have while reaching each house
        dp[0]=nums[0] #for first house only one option
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            #two possibilities, you either pick a house or you don't
            pick,nopick=0,0
            
            #1.Pick
            pick=nums[i]+dp[i-2]
            
            #2.Don't pick
            nopick=dp[i-1]
            
            dp[i]=max(pick,nopick)
        return dp[n-1] #last house


        