"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

"""


"""
approach

use the dfs recusively to eexploare all the brnahces horizontal and verttical 
make the toched node as 0 
traverse all the points till end of the materix 
mantain a counter for island


"""



class Solution:

	def dfs(self,i,j,grid):
		"""
		The function to do the dfs serach
		"""
		#get the length and width
		length = len(grid[0])
		width = len(grid)

		if i < 0 or j < 0 or i >= width or j >= length or grid[i][j] == "0":
			return None

		# Mark the current cell as visited
		grid[i][j] = "0"

		self.dfs(i,j-1,grid)
		self.dfs(i,j+1,grid)
		self.dfs(i-1,j,grid)
		self.dfs(i+1,j,grid)


	def numIslands(self, grid) -> int:
		"""
		The function to find the number of islands
		The code passes leetcode
		"""
		
		#get the length and width
		length = len(grid[0])
		width = len(grid)
		count_island = 0 

		for i in range(width):
			for j in range(length):

				if grid[i][j] == "1":
					count_island +=1
				
				self.dfs(i,j,grid)
		
		return count_island
	