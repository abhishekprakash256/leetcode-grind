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


class Solution_slow():
	"""
	This is a slow soln
	"""

	def __init__(self):

		self.min_val = float("inf")

	def helper_dfs(self, i,j,curr_sum) -> int:
		"""
		The function for helper dfs
		"""

		#print(i,j)

		if i == self.row and j == self.col:

			self.min_val = min(self.min_val,curr_sum + self.grid[i][j])

			return

		#make the base case 
		if i > self.row or j > self.col:

			return


		#dfs recurstion call 
		right = self.helper_dfs(i , j + 1 , curr_sum + self.grid[i][j])
		down = self.helper_dfs(i + 1, j , curr_sum + self.grid[i][j])



		
	def minPathSum(self, grid) -> int:
		"""
		The function to find the min path sum 

		"""
		self.grid = grid
		self.row = len(self.grid) - 1 
		self.col = len(self.grid[0]) - 1 

		#constraints 
		if len(self.grid) == 1 and len(self.grid[0]) == 1:
			
			return self.grid[0][0]

		#make the vars
		i = j = curr_sum = 0 

		self.helper_dfs(i,j,curr_sum)

		return self.min_val










class Solution_memo():
	"""
	This is a slow soln 
	accepted in leetcode
	"""

	def __init__(self):

		self.memo = {}

	def helper_dfs(self, i,j) -> int:
		"""
		The function for helper dfs
		"""

		#print(i,j)

		if i == self.row and j == self.col:

			return self.grid[i][j]


		#make the base case 
		if i > self.row or j > self.col:

			return float("inf")

		#get from the memo
		if (i,j) in self.memo :

			return self.memo[(i,j)]


		#dfs recurstion call 
		right = self.helper_dfs(i , j + 1)
		down = self.helper_dfs(i + 1, j )

		self.memo[(i,j)] = self.grid[i][j] + min(right , down)

		return self.memo[(i,j)]



		
	def minPathSum(self, grid) -> int:
		"""
		The function to find the min path sum 

		"""
		self.grid = grid
		self.row = len(self.grid) - 1 
		self.col = len(self.grid[0]) - 1 

		#constraints 
		if len(self.grid) == 1 and len(self.grid[0]) == 1:
			
			return self.grid[0][0]

		#make the vars
		i = j = 0 

		return self.helper_dfs(i,j)







class Solution():

	def minPathSum(self,grid):
		"""
		The function to find the minpath using dp
		passes leetcode fastest solution
		"""

		#constraints 
		if len(grid) == 1 and len(grid[0]) == 1:
			
			return grid[0][0]

		m, n = len(grid), len(grid[0])
		
		# Fill the first row
		for j in range(1, n):
			grid[0][j] += grid[0][j-1]
		
		# Fill the first column
		for i in range(1, m):
			grid[i][0] += grid[i-1][0]
		
		# Fill the rest of the grid
		for i in range(1, m):
			for j in range(1, n):
				grid[i][j] += min(grid[i-1][j], grid[i][j-1])
		







sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))




		