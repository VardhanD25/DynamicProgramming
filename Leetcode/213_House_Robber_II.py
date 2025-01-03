#https://leetcode.com/problems/house-robber-ii/
class Solution(object):
    def rob(self, nums):
        #Using the same code from House Robber 1
        #We just need to consider 2 cases 
        #1) Array without last element
        #2) Array without first element
        #Since array is circular, first and last are adjacent, thus they
        #cannot be picked at the same time
        #If we consider two cases the problems breaks down into 2 subproblems
        #Our answer will be the max of these two problems
        def helper(nums):
            n=len(nums)
            if n==0:
                return 0
            if n==1:
                return nums[0]
            dp=[0]*n  #stores max money you can have while reaching each house
            dp[0]=nums[0]  #for first house only one option
            dp[1]=max(nums[0],nums[1])
            for i in range(2,n):
            #Two possibilities, you either pick a house or you don't
                pick,nopick=0,0
            
                #1.Pick
                pick=nums[i]+dp[i-2]
            
                #2.Don't pick
                nopick=dp[i-1]
            
                dp[i]=max(pick,nopick)
            return dp[n-1] #last house
        #Special case as if length is 1 this element will be missed in both arrays
        if len(nums)==1:
            return nums[0]
        withoutFirst=nums[1:]
        withoutLast=nums[:len(nums)-1]
        return max(helper(withoutFirst),helper(withoutLast))
        