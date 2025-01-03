#https://leetcode.com/problems/unique-paths/
class Solution(object):
    def uniquePaths(self, m, n):
        dp=[[-1]*n for _ in range(m)]
        def recur(x,y):
            if x>=m or y>=n:
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
        