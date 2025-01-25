"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

"""


"""

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.



"""


class Solution():
	"""
	passes leetcode
	"""

	def __init__(self):

		self.count = 0

	def helper_dfs(self,i,j):
		"""
		The function to do the dfs traversal for the grid
		"""

		#base case 
		if i < 0 or j < 0 or i > self.row - 1 or j > self.col - 1  or self.grid[i][j] == "0":

			return

		#make the grid "0"
		self.grid[i][j] = "0"

		#make the recursive call
		up = self.helper_dfs(i-1,j)
		down = self.helper_dfs(i+1,j)
		left = self.helper_dfs(i,j-1)
		right = self.helper_dfs(i,j+1)



	def numIslands(self,grid):
		"""
		The function to find the number of the islands in the grid 
		"""

		#make the vars
		self.grid = grid

		self.row = len(self.grid)
		self.col = len(self.grid[0])

		#iterate the rows and the cols 
		for i in range(self.row) :

			for j in range(self.col) :

				if self.grid[i][j] == "1" :

					self.count += 1 

				self.helper_dfs(i,j)

		return self.count





		

