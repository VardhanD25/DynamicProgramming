#https://leetcode.com/problems/unique-paths-ii/
#Extension of 62.Unique Paths

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1]*n for _ in range(m)]
        def recur(x,y):
            if x>=m or y>=n:
                return 0
            #only extra condition required for detecting obstacle
            if obstacleGrid[x][y]==1:
                return 0
            if x==m-1 and y==n-1:
                return 1
            if dp[x][y]!=-1:
                return dp[x][y]
            
            right=recur(x+1,y)
            down=recur(x,y+1)
            dp[x][y]=right+down
            return dp[x][y]
        return recur(0,0)
        