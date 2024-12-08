"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""

"""
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


"""


"""
approach - 

make a dfs solution using the  



"""



class Solution(object):

	def dfs_graph(self,i,j):
		"""
		The function to get the dfs of the graph
		"""

		#base case 
		if self.grid[i][j] == "0" or i < 0 or j > len(self.grid[0]) - 1  or i > len(self.grid)-1 or j < 0 :

			return None


		#make the grid 0 
		self.grid[i][j] = "0"

		#make the dfs graph call 
		self.dfs_graph(i-1,j)
		self.dfs_graph(i+1,j)
		self.dfs_graph(i,j-1)
		self.dfs_graph(i,j-1)





	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""

		self.grid = grid
		count = 0 


		#make the iterative search
		for i in range(len(self.grid)-1) :

			for j in range(len(self.grid[0])-1) :

				if self.grid[i][j] == "1":

					count +=1
				
				self.dfs_graph(i,j)

		return count

