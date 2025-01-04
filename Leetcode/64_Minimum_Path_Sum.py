#https://leetcode.com/problems/minimum-path-sum/

class Solution(object):
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        def recur(x,y):
            if x>=m or y>=n:
                return float('inf') #return large number so that path gets discarded
            if x==m-1 and y==n-1:
                return grid[m-1][n-1]
            if dp[x][y]!=-1:
                return dp[x][y]
            
            right=recur(x,y+1)
            down=recur(x+1,y)
            dp[x][y]=grid[x][y]+min(right,down)
            return dp[x][y]
        return recur(0,0)

        