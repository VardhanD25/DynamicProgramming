#https://leetcode.com/problems/burst-balloons/

#Memoization approach
class Solution(object):
    def maxCoins(self, nums):
        n=len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp=[[-1]*(n+1) for _ in range(n+1)]

        def recur(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi=float('-inf')
            for ind in range(i,j+1):
                cost=nums[i-1]*nums[ind]*nums[j+1]+recur(i,ind-1)+recur(ind+1,j)
                maxi=max(maxi,cost)
            dp[i][j]=maxi
            return maxi
        return recur(1,n)

#Tabulation approach
class Solution(object):
    def maxCoins(self, nums):
        n=len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp=[[0]*(n+2) for _ in range(n+2)]

        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                maxi=float('-inf')
                for ind in range(i,j+1):
                    cost=nums[i-1]*nums[ind]*nums[j+1]+dp[i][ind-1]+dp[ind+1][j]
                    maxi=max(maxi,cost)
                dp[i][j]=maxi
        return dp[1][n]
