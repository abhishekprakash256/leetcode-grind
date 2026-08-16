"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.


"""

"""
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true



Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


"""



"""
approach -- 

grid search and then append all the values and match the value

bounding case , for exit 

make a temp list to match


"""

from typing import List



class Solution:

	def __init__(self) :

		self.res = False


	def _helper(self , word_str  , i , j , visited ):
		"""
		The function to find the word in the board
		"""

		#print( i , j )

		#base case
		# Boundary check
		if (
			i < 0
			or i >= len(self.board)
			or j < 0
			or j >= len(self.board[0])
		):
			return
		

		#find the word
		if len(word_str) > len(self.word) :

			return

		#match the word
		if word_str == self.word :

			self.res = True

			return


		#mark the visisted
		visited.add((i,j))

		# Add current cell
		word_str += self.board[i][j]

		#call the helper function for search
		self._helper( word_str  , i , j + 1 , visited )

		self._helper( word_str  , i + 1 , j , visited )

		self._helper( word_str , i, j - 1 , visited )

		self._helper( word_str , i - 1 , j , visited )

		visited.remove(( i , j))

		




	def exist(self, board: List[List[str]], word: str) -> bool:
		"""
		The function to find the word in the board
		"""

		#the search board
		self.board = board
		self.word = word

		#vars
		word_str = ""

		#make a visited set
		visited = set()

		#iter over the function 
		for i in range(len(self.board)) :

			for j in range(len(self.board[0])): 

				#call the helper function 
				self._helper( word_str , i , j , visited )

				if self.res :

					return True


		return self.res






#testing the solution 
if __name__ == '__main__':

	board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

	word = "ABCCED"

	sol = Solution()

	res = sol.exist( board , word )

	print(res)

















