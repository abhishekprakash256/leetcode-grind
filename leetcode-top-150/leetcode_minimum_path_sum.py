"""

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 

which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


"""
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

"""

"""
approach -- 

using the helper_dfs track the values 

#make the base case 

if i >= len(self.board) or j >= len(self.board[0]) :

	#add the value

	return 

maintan the min value 

"""


class Solution():

	def __init__(self):

		self.min_val = self.float("inf")
		
	def minPathSum(self, grid: List[List[int]]) -> int:
		"""
		The function to find the min path sum 

		"""
		self.grid = grid
		self.row = len(self.grid)
		self.col = len(self.grid[0])

		#constraints 
		if self.row == 1 :

			if self.col == 1 :

				return self.grid[0][0]



		