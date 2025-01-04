#https://leetcode.com/problems/triangle/

class Solution(object):
    def minimumTotal(self, triangle):
        rows=len(triangle)
        dp=[[-1]*(i+1) for i in range(rows)]
        
        def recur(row,index):
            if row>=rows:
                return 0
            if dp[row][index]!=-1:
                return dp[row][index]
            down1=recur(row+1,index)
            down2=recur(row+1,index+1)
            dp[row][index]=triangle[row][index]+min(down1,down2)
            return dp[row][index]
        return recur(0,0)
        