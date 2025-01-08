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


class Solution():

	def __init__(self):

		self.min_sum = float("inf")


	def helper_dfs(self,i,j,carry_sum):
		"""
		The helper dfs function to calculate the sum
		"""
		#base case 

		#not pass the boundary

		#maintatin a copy of the map to not make the search again 

		#with update the min sum 
		pass


	def minimumTotal(self,triangle):
		"""
		The function to find the min path sum in the trinage
		"""

		#constarints 
		if len(triangle) == 1:

			if len(triangle[0]) == 1 :

				return triangle[0][0]


		#start the dfs traversal 
		#how to get the number of traversal from top ? 

