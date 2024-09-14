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



class Solution():

	def helper(self,i,j,m,n):
		"""
		The helper function for dfs
		"""

		#base case 
		if i == m -1 and j == n- 1:
			return 1

		if i >= m or j >= n :
			return 0


		#down_traveral 
		down = self.helper(i,j + 1,m,n)
		rigt = self.helper(i + 1,m,n)


		return down + right


	def uniquePaths(self, m, n):
		"""
		The main function to calculate unique paths in a grid.
		"""

		# Constraint case: if the grid is 1x1, there's only 1 unique path
		if m == 1 and n == 1:
			return 1

		# Call the recursive helper starting from the top-left corner (0, 0)
		return self.helper(0, 0, m, n)
