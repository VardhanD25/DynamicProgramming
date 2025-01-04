#https://leetcode.com/problems/minimum-falling-path-sum/

class Solution(object):
    def minFallingPathSum(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Create a dp table initialized with the last row of the matrix
        dp = [[0] * cols for _ in range(rows)]
        for j in range(cols):
            dp[rows - 1][j] = matrix[rows - 1][j]

        # Fill the dp table from the second-last row upwards
        for row in range(rows - 2, -1, -1):
            for col in range(cols):
                # Compute the minimum path sum for each cell
                down1 = dp[row + 1][col - 1] if col > 0 else float('inf')  # Diagonal left
                down2 = dp[row + 1][col]  # Directly below
                down3 = dp[row + 1][col + 1] if col < cols - 1 else float('inf')  # Diagonal right
                dp[row][col] = matrix[row][col] + min(down1, down2, down3)

        # The answer is the minimum value in the first row of dp
        return min(dp[0])
