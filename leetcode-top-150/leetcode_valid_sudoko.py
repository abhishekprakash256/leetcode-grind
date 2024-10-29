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



class Solution:
	#dfs 
	def dfs(self,i,j,mapper):

		#base case 
		if i == i + 3 or j == j + 3 :
			return
		
		self.dfs(i+1 , j, mapper)
		self.dfs(i,j + 1, mapper)

		if self.board[i][j] not in mapper:
			mapper[self.board[i][j]] = True
		
		else:
			return False
		

	def isValidSudoku(self, board: list) -> bool:
		"""
		The function to find the sudo is valid
		"""

		#vars 
		row = len(board)
		col = len(board[0])
		self.board = board


		#row checking 
		for i in range(row):

			mapper = {}

			for j in range(col):
				
				if board[i][j] not in mapper:
					
					mapper[board[i][j]] = True
				
				else:
					return False


		#column checking 
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

				mapper = {}
				
				if self.dfs(i,j, mapper) != True:
					return False
				
		
		return True




