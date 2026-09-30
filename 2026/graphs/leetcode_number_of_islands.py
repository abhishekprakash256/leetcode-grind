"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
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
from typing import List



class Solution:
	def __init__(self):

		self.count = 0

		self.visited = set()


	def dfs_helper(self , x , y):
		"""
		The function for the dfs traversal
		"""

		#condition limits
		if x < 0 or x >= self.rows or y < 0 or y >= self.cols:
			
			return

		if self.grid[x][y] == "0":

			return

		#mark the grid 
		self.grid[x][y] = "0"

		#travers the dirs
		for dir_x , dir_y in self.dirs :

			new_x , new_y = dir_x + x , dir_y + y

			#make the recuresion
			self.dfs_helper(new_x , new_y)





	def numIslands(self, grid: List[List[str]]) -> int:
		"""
		The function to find the number of the islands
		"""

		self.grid = grid

		self.rows = len(self.grid)

		self.cols = len(self.grid[0])

		self.dirs = [
		(1,0),
		(-1,0),
		(0,1),
		(0,-1)
		]

		#traverse the grid 
		for i in range(self.rows) :


			for j in range(self.cols) :


				if self.grid[i][j] == "1" :

					self.count += 1 

					self.dfs_helper( i , j )


		return self.count




if __name__ == "__main__":

	sol = Solution()

	grid = [
	["1","1","0","0","0"],
	["1","1","0","0","0"],
	["0","0","1","0","0"],
	["0","0","0","1","1"]
	]

	res = sol.numIslands(grid)

	print(res)