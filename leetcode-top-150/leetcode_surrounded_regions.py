"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

	Connect: A cell is connected to adjacent cells horizontally or vertically.
	Region: To form a region connect every 'O' cell.
	Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.

A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.


"""


"""

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]



Input: board = [["X"]]

Output: [["X"]]



"""


"""
approach -- 

use a dfs search on each point and then check and return True

base case
if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1
	return False

if grid[i][j] == "X" :
	
	return True 


if self.dfs(i-1,j) and self.dfs(i+1,j) and self.dfs(i,j-1) and  self.dfs(i,j-1) :
	grid[i][j] = "X"




"""


inp = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]




class Solution:

	def dfs_search(self,i,j):
		"""
		The function to do the dfs search
		"""

		#base case
		if i < 0 or j < 0 or i > len(self.board) - 1 or j > len(self.board[0]) - 1 or self.board[i][j] == "#" :

			return False


		self.board[i][j] = "#" 

		
		#call the dfs recursive
		up = self.dfs_search(i-1,j)
		down = self.dfs_search(i+1,j) 
		left = self.dfs_search(i,j-1)
		right = self.dfs_search(i,j+1)




	def solve(self, board) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""

		self.board = board


		#iteration 
		
		for i in range(len(self.board)):

			for j in range(len(self.board[0])) :

				self.dfs_search(i,j)




if __name__ == '__main__':
	sol = Solution()

	sol.solve(inp)

	print(inp)








