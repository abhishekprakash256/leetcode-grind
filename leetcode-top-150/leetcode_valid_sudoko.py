"""

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.


"""




"""
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


"""


"""

brute force approach -- 

row = len(board)
col = len(board[0])


rows , col and block ( 3 X 3 check )



3 way checking 
	- one for row 
	- one for column 
	- one for square blocks

	
#column 

for i in range(row):

	mapper = {}

	for j in range(col):
		
		if board[i][j] not in mapper:
			
			mapper[board[i][j]] = True
		
		else:
			return False
		

#row
	   
for i in range(row):

	mapper = {}

	for j in range(col):
		
		if board[j][i] not in mapper:
			
			mapper[board[j][i]] = True
		
		else:
			return False


			

#check the 3X3 cube 

for i in range(0,3,row):

	for j in range(0,3,col):
		
		if dfs(board[i][j]) != True:
			return False


			
#make the dfs 

def dfs(board[i][j], mapper):

	#base case 
	if i == i + 3 and j == j + 3 :
		return
	
	self.dfs(i+1 , j)
	self.dfs(i,j + 1)

	if board[i][j] not in mapper:
		mapper[board[i][j]] = True
	
	else:
		return False



	
			


"""



class Solution_brute:
	# Helper function for 3x3 grid validation
	def dfs(self, i, j, mapper):
		"""
		Recursive function to check a 3x3 grid.
		"""
		# Base case: stop when reaching the boundaries of a 3x3 grid
		if i == 3 or j == 3:
			return True
		
		# Check if the current cell is valid
		if self.board[self.start_i + i][self.start_j + j] != ".":
			num = self.board[self.start_i + i][self.start_j + j]
			if num in mapper:
				return False
			mapper[num] = True
		
		# Recursively move to the next cell in the 3x3 grid
		if j < 2:
			return self.dfs(i, j + 1, mapper)
		else:
			return self.dfs(i + 1, 0, mapper)

	def isValidSudoku(self, board: list) -> bool:
		"""
		Validates the Sudoku board.
		passes leetcode
		"""
		self.board = board


		# Row validation
		for i in range(9):
			row_mapper = {}
			for j in range(9):
				if self.board[i][j] != ".":
					if self.board[i][j] in row_mapper:
						return False
					row_mapper[self.board[i][j]] = True

		
		# Column validation
		for j in range(9):
			col_mapper = {}
			for i in range(9):
				if self.board[i][j] != ".":
					if self.board[i][j] in col_mapper:
						return False
					col_mapper[self.board[i][j]] = True

		
		# 3x3 subgrid validation using dfs
		for i in range(0, 9, 3):
			for j in range(0, 9, 3):
				self.start_i, self.start_j = i, j  # Starting coordinates for the 3x3 grid
				subgrid_mapper = {}
				if not self.dfs(0, 0, subgrid_mapper):  # Start dfs within each 3x3 grid
					return False

		return True





from typing import List

class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		"""
		Function to check if a Sudoku board is valid.
		"""

		# Row validation
		for i in range(9):
			row_mapper = {}
			for j in range(9):
				if board[i][j] != ".":
					if board[i][j] in row_mapper:
						return False
					row_mapper[board[i][j]] = True

		# Column validation
		for i in range(9):
			col_mapper = {}
			for j in range(9):
				if board[j][i] != ".":
					if board[j][i] in col_mapper:
						return False
					col_mapper[board[j][i]] = True

		# 3x3 subgrid validation
		for i in range(0, 9, 3):
			for j in range(0, 9, 3):
				subgrid_mapper = {}
				for x in range(i, i + 3):
					for y in range(j, j + 3):
						if board[x][y] != ".":
							if board[x][y] in subgrid_mapper:
								return False
							subgrid_mapper[board[x][y]] = True

		# If all checks pass, the board is valid
		return True








