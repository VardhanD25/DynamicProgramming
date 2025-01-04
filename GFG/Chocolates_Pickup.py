#https://www.geeksforgeeks.org/problems/chocolates-pickup/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=chocolates-pickup

class Solution:
    def solve(self, n, m, grid):
        # Initialize two 2D arrays for storing previous and current row DP values
        prev_dp = [[-1] * m for _ in range(m)]

        # Base case: Initialize the last row
        for col1 in range(m):
            for col2 in range(m):
                if col1 == col2:
                    prev_dp[col1][col2] = grid[n - 1][col1]
                else:
                    prev_dp[col1][col2] = grid[n - 1][col1] + grid[n - 1][col2]

        # Iterate from second-last row to the first row
        for row in range(n - 2, -1, -1):
            # Create a new DP table for the current row
            curr_dp = [[-1] * m for _ in range(m)]

            for col1 in range(m):
                for col2 in range(m):
                    max_val = float('-inf')

                    # Explore all possible movements
                    for i in range(-1, 2):  # Move for col1
                        for j in range(-1, 2):  # Move for col2
                            new_col1 = col1 + i
                            new_col2 = col2 + j

                            if 0 <= new_col1 < m and 0 <= new_col2 < m:
                                if col1 == col2:
                                    val = grid[row][col1]
                                else:
                                    val = grid[row][col1] + grid[row][col2]

                                val += prev_dp[new_col1][new_col2]
                                max_val = max(max_val, val)

                    curr_dp[col1][col2] = max_val

            # Update `prev_dp` for the next iteration
            prev_dp = curr_dp

        # The answer is the maximum value for starting at the first row
        return prev_dp[0][m - 1]
