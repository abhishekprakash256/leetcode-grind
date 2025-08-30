"""
To get the number of island in the in the grid matrix

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

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


"""


"""
start the traversal and the direction of the points 
then dfs and make it zero and keep the count


"""


from typing import List


class Solution:

	def dfs(self,i,j):
		"""
		The method of the dfs traversal
		"""

		#the edge condn
		if i < 0 or i >= self.row or j < 0 or j >= self.col or self.grid[i][j] == "0":
			
			return

		#make the grid 0 
		self.grid[i][j] = "0"

		#traversal in the dirs 
		self.dfs(i - 1 , j )
		self.dfs(i + 1 , j )
		self.dfs(i , j - 1 )
		self.dfs(i , j + 1 )


	

	def numIslands(self, grid: List[List[str]]) -> int:
		"""
		The method to find the number of the island 
		"""

		#get the dims of the grid
		self.row = len(grid) 
		self.col = len(grid[0]) 

		#the grid
		self.grid = grid

		count = 0

		#find the 1's in the grid iter the grid
		for i in range(self.row) :

			for j in range(self.col) :

				#find the 1's in the grid
				if self.grid[i][j] == "1" :

					count += 1

					#iter the dfs
					self.dfs(i,j)

		return count




if __name__ == "__main__":
	
	grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

	sol = Solution()

	res = sol.numIslands(grid)

	print(res)











