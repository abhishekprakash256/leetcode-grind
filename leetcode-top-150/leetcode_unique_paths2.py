"""
You are given an m x n integer array grid. There is a robot initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner
 (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point 
 in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot 
takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the 
bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


"""

"""
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

"""


"""
approach -- 

traking the qunique paths 

make a global count 
self.count = 0 

add the base cases 
if i == m and j == n :

	self.count += 1

if i > m or j > n or grid[i][j] == 1:
	return 

#constarint case 
if len(grid) == 1 and len(grid[0]) == 1:

	return 1 


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
"""


class Solution_slow():
	"""
	Slow solution
	"""

	def __init__(self):

		self.count = 0

	def helper_dfs(self,i,j):
		"""
		The helper funciton for the dfs 
		"""
		#make the row and col vars
		row = len(self.obstacleGrid) - 1	
		col = len(self.obstacleGrid[0]) - 1

		#base case 
		if i == row and j == col :

			self.count += 1
			return 

		if i > row or j > col or self.obstacleGrid[i][j] == 1 :

			return

		#make the dfs calls 
		self.helper_dfs(i,j+1)
		self.helper_dfs(i+1,j)



	def uniquePathsWithObstacles(self,obstacleGrid ):
		"""
		The function to find the totatl number of unique paths 
		"""

		#constarints case 
		if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:

			if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1: 

				return 0

			else:

				return 1 

		#contarint last is 1
		if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:

			return 0

		#make the vars
		self.obstacleGrid = obstacleGrid

		#pinters 
		i = j = 0

		#make the recursion call
		self.helper_dfs(i,j)

		return self.count




class Solution_memo():
	"""
	Slow solution
	passes leetcode
	"""

	def __init__(self):

		self.memo = {}


	def helper_dfs(self,i,j):
		"""
		The helper funciton for the dfs 
		"""
		#make the row and col vars
		row = len(self.obstacleGrid) - 1	
		col = len(self.obstacleGrid[0]) - 1

		if (i,j) in self.memo:

			return self.memo[(i,j)]

		#base case 
		if i == row and j == col :

			return 1

		if i > row or j > col or self.obstacleGrid[i][j] == 1 :

			return 0


		#make the dfs calls 
		right = self.helper_dfs(i,j+1)
		down = self.helper_dfs(i+1,j)

		self.memo[(i,j)] = right + down

		return self.memo[(i,j)]



	def uniquePathsWithObstacles(self,obstacleGrid ):
		"""
		The function to find the totatl number of unique paths 
		"""

		#constarints case 
		if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:

			if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1: 

				return 0

			else:

				return 1 

		#contarint last is 1
		if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:

			return 0

		#make the vars
		self.obstacleGrid = obstacleGrid

		#pinters 
		i = j = 0

		#make the recursion call
		return self.helper_dfs(i,j)



class Solution():


	def uniquePathsWithObstacles(self,obstacleGrid ):
		"""
		The function to find the number of unique Paths

		"""

		#constarints case 
		if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:

			if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1: 

				return 0

			else:

				return 1 

		#contarint last is 1
		if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:

			return 0



class Solution:
    """
    DP solution for unique paths with obstacles.
    passes leetcode
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        Find the total number of unique paths using dynamic programming.
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # If the start or end point is blocked, there are no paths
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        # Create a DP table to store the number of unique paths to each cell
        dp = [[0] * cols for _ in range(rows)]

        # Base case: Starting position has one path if not blocked
        dp[0][0] = 1

        # Fill the DP table
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # No paths through an obstacle
                else:
                    if i > 0:  # Add paths from the cell above
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:  # Add paths from the cell to the left
                        dp[i][j] += dp[i][j - 1]

        # The value at the bottom-right corner is the total number of unique paths
        return dp[rows - 1][cols - 1]
