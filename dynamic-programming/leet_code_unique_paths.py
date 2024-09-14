"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 
"""


"""
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""



class Solution_brute_force():

	def __init__(self):
		
		self.memo = {}

	def helper_brute_force(self,i,j,m,n):
		"""
		The helper function for dfs
		"""

		#base case 
		if i == m -1 and j == n- 1:
			return 1

		if i >= m or j >= n :
			return 0


		#down_traveral 
		down = self.helper_brute_force(i,j + 1,m,n)
		rigt = self.helper_brute_force(i + 1,m,n)


		return down + right


	def uniquePaths_brute_force(self, m, n):
		"""
		The main function to calculate unique paths in a grid.
		"""

		# Constraint case: if the grid is 1x1, there's only 1 unique path
		if m == 0 and n == 0:
			return 1

		# Call the recursive helper starting from the top-left corner (0, 0)
		return self.helper_brute_force(0, 0, m, n)







class Solution_memo:

	def __init__(self):
		self.memo = {}  # Dictionary to store results of subproblems.

	def helper(self, i, j, m, n):
		"""
		The function to count unique paths using DFS with memoization.
		"""

		# Base case: if we reach the bottom-right corner, there's only 1 path.
		if i == m - 1 and j == n - 1:
			return 1

		# Base case: if we go out of bounds, there's no valid path.
		if i >= m or j >= n:
			return 0

		# If we have already calculated the number of paths from this position, return it.
		if (i, j) in self.memo:
			return self.memo[(i, j)]

		# Recursive case: move right (j+1) and move down (i+1).
		right_paths = self.helper(i, j + 1, m, n)  # Move right
		down_paths = self.helper(i + 1, j, m, n)   # Move down

		# Store the result in memo dictionary and return it.
		self.memo[(i, j)] = right_paths + down_paths

		return self.memo[(i, j)]

	def uniquePaths(self, m, n):
		"""
		The main function to calculate unique paths in a grid of size m x n.
		passes leet code
		"""

		#constraints
		if m == 0 and n == 0:
			return 1


		return self.helper(0, 0, m, n)  # Start from the top-left corner.




class Solution_dp:

    def uniquePaths(self, m, n):
        """
        The function to calculate unique paths using dynamic programming.
        """
        # Create a 2D DP array with size m x n
        dp = [[0] * n for _ in range(m)]

        # Initialize the first row and first column to 1
        for i in range(m):
            dp[i][0] = 1  # There's only one way to move down the first column
        for j in range(n):
            dp[0][j] = 1  # There's only one way to move right in the first row

        # Fill the DP table using the recurrence relation
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # The value at dp[m-1][n-1] will be the number of unique paths
        return dp[m-1][n-1]





