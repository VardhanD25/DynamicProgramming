#https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution(object):
    def countSquares(self, matrix):
        rows,cols=len(matrix),len(matrix[0])
        dp=[[0]*cols for _ in range(rows)]
        sumi=0
        for i in range(rows):
            dp[i][0]=matrix[i][0]

        for j in range(cols):
            dp[0][j]=matrix[0][j]
            
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
        sumi=0
        for i in range(rows):
            for j in range(cols):
                sumi+=dp[i][j]
        return sumi
        
        