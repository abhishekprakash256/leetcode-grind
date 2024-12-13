"""
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.
"""



"""
Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.


"""


"""
approach -- 

use a hashmap to maitain the key and match the column 


mapper = {}


if the row not in mapper or flipped_row  not in mapper :
	mapper[tuple(row)] = 1 

else:

	mapper[tuple(row)] = mapper[tupple(row)] + 1 

return max(mapper.count)

"""



class Solution:
	def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
		"""
		The function to check for the max number of rows that can be matched
		"""

		#base case 
		if len(matrix) == 1 :

			return 0 

		#make the hashmap
		mapper = {}


		#make the matrix 
		for row in matrix:

			if tuple(row) not in mapper : 

				mapper[tuple(row)] = 1 

			else :

				flipped_row = [1 - x for x in row]

				if tuple(flipped_row) in mapper :

					mapper[tuple(flipped_row)] = mapper[tuple(flipped_row)] + 1

				else:

					mapper[tuple(row)] = mapper[tuple(row)] + 1
		

		return max(mapper.values())

		 


			





