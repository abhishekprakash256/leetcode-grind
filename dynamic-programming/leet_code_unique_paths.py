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
		The helper function to do the dfs
		"""

		#base case 
		if i == m - 1 and j == n - 1 :
			return True

		#base case out of bound 
		if i > m - 1 or j > n -1 :
			return False


		#make the function call 
		self.helper(i + 1, j)
		self.helper(i, j + 1)

		#make the count 


	def uniquePaths(self,m,n):
		"""
		The main path function
		"""

		count = 0 

		#constaint case 
		if m == 1 and n == 1 :
			return 1


		self.helper(0,0,m,n)


		return count