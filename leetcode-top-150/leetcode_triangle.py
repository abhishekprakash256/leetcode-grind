"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, 
you may move to either index i or index i + 1 on the next row.
"""

"""
Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
	2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10


Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104

"""

"""
approach --

exhaust all the possiblites 

from top to bottom and return the least value 

can not choose min at each step it can cost more at later 

one is greedy approch

move only i, i+ 1 on the next row 

making and dfs can be used the restrcition of movemmet can be used in dfs next as i and i + 1 on the next row

with getting the value and memoization can be done for faster 

cal the value in all and give min by maintaing the global min value 

"""


class Solution_slow():
	"""
	It is a slow solution

	"""

	def __init__(self):

		self.min_sum = float("inf")


	def helper_dfs(self,i,j,carry_sum, path):
		"""
		The helper dfs function to calculate the sum
		"""

		#base case
		if i >= len(self.triangle) - 1 or j >= len(self.triangle[i+1])-1 :  #or self.triangle == "#": #make more condn

			self.min_sum = min(self.min_sum, carry_sum + self.triangle[i][j])

			return

		#marked the search area
		#self.temp_board[i][j] = "#"


		#make the dfs traversal 
		first_pos = self.helper_dfs(i+1,j, carry_sum + self.triangle[i][j], path + str(self.triangle[i][j]) )
		second_pos = self.helper_dfs(i+1,j+1, carry_sum + self.triangle[i][j], path + str(self.triangle[i][j]))



	def minimumTotal(self,triangle):
		"""
		The function to find the min path sum in the trinage
		"""

		self.triangle = triangle

		#constarints 
		if len(triangle) == 1:

			if len(triangle[0]) == 1 :

				return triangle[0][0]

		#sum var
		carry_sum = 0 

		#initial coordinate
		i = j = 0 

		path = ""

		#start the dfs traversal
		self.helper_dfs(i,j,carry_sum, path)

		return self.min_sum



class Solution_memo:
"""
Passes leet code 

"""

def __init__(self):
	self.memo = {}

	def helper_dfs(self, i, j):
		"""
		The helper function to calculate the minimum path sum using DFS with memoization.
		"""
		# Base case: If we're at the last row, return the value at (i, j)
		if i == len(self.triangle) - 1:
			return self.triangle[i][j]

		# Check memo
		if (i, j) in self.memo:
			return self.memo[(i, j)]

		# Recursive DFS calls
		left_path = self.helper_dfs(i + 1, j)
		right_path = self.helper_dfs(i + 1, j + 1)

		# Store the result in memo
		self.memo[(i, j)] = self.triangle[i][j] + min(left_path, right_path)
		return self.memo[(i, j)]

	def minimumTotal(self, triangle):
		"""
		The function to find the minimum path sum in the triangle.
		"""
		self.triangle = triangle

		# Edge case: single element triangle
		if len(triangle) == 1 and len(triangle[0]) == 1:
			return triangle[0][0]

		# Start DFS from the top of the triangle
		return self.helper_dfs(0, 0)




class Solution():

	def minimumTotal(self,triangle):
		"""
		The function to make the minimum sum
		passes leetcode
		"""
		# Edge case: single element triangle
		if len(triangle) == 1 and len(triangle[0]) == 1:
			return triangle[0][0]

		#make the dp array 
		dp = triangle[-1][:]

		#make the sum
		for i in range(len(triangle) - 2,-1,-1):

			for j in range(len(triangle[i])) :

				dp[j] = triangle[i][j] + min(dp[j],dp[j+1])

		return dp[0] 






sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))


