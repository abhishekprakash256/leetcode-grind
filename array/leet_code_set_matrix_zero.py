"""
set the matrix to zero
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
in place 
"""

matrix = [[1,1,1],[1,0,1],[1,1,1]]
out = [[1,0,1],[0,0,0],[1,0,1]]


matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
out2 = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


#correct soln is the second one 

class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""

		num_rows = len(matrix)
		num_cols = len(matrix[0])

		zero_loc_lst = []


		for i in range(num_rows):

			for j in range(num_cols):

				#find the zero location
				if matrix[i][j] == 0:

					zero_loc_lst.append([i,j])


		#start the iteration of the zero loc list 

		for pos_x, pos_y in zero_loc_lst:

			#start the filling algorithm

			#start the vertical up filling
			while matrix[pos_x - 1][pos_y]:

				matrix[pos_x -1][pos_y] = 0

				pos_x -=1


			#start the vertical down filling algorithm
			while matrix[pos_x +1][pos_y]:

				matrix[pos_x + 1][pos_y] = 0
				pos_x +=1


			#strat the horizaontal left filling 
			while matrix[pos_x][pos_y - 1]:

				matrix[pos_x][pos_y - 1] = 0
				pos_y -=1


			#start the horizaontal right filling
			while matrix[pos_x][pos_y +1]:

				matrix[pos_x][pos_y + 1] = 0
				pos_y +=1


		return matrix


	def setZeroes2(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""

		num_rows = len(matrix)
		num_cols = len(matrix[0])

		zero_rows = set()
		zero_cols = set()

		# Find the zero locations
		for i in range(num_rows):
			for j in range(num_cols):
				if matrix[i][j] == 0:
					zero_rows.add(i)
					zero_cols.add(j)

		# Set entire rows to zero
		for row in zero_rows:
			for j in range(num_cols):
				matrix[row][j] = 0

		# Set entire columns to zero
		for col in zero_cols:
			for i in range(num_rows):
				matrix[i][col] = 0

		return matrix






if __name__ == "__main__":

	sol = Solution()
	res = sol.setZeroes2(matrix)


	print(res)