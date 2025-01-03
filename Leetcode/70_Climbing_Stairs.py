#https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        #Same as fibonacci series
        #Base cases: n=1 and n=2
        #For n=1 , only 1 way to get there
        #For n=2, 2 ways, 1+1 and 2
        if n==1:
            return 1
        if n==2:
            return 2

        ways=[0]*(n+1) #stores number of ways to get to nth step
        ways[1]=1
        ways[2]=2
        for i in range(3,n+1):
            #root=left tree +right tree
            ways[i]=ways[i-1]+ways[i-2]

        return ways[n]
        