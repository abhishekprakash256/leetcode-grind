"""
You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.

A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:

It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.
"""


"""


Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to bottom).


Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
Output: false
Explanation: It is impossible to place the word because there will always be a space/letter above or below it.

Example 3:

Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
Output: true
Explanation: The word "ca" can be placed as shown above (right to left). 

"""



"""
appraoch -- 

dfs when I found the letter and found the empty space that is need 

found the empty space ? 

when I foubd empty space seach for remaining letter space only if more discard 

if # igonre 

when found a char use DFS to find the number of space and no extra space in vertical and horizontal

how get vertical and horizontal space  ? 

initilaize count there and count increase and count == len(reamain)

empty space as well ?

look for two space or three space ? how ? 




"""


class Solution():

	def helper_dfs(self,i,j):
		"""
		The helper function to do the dfs 
		"""

		pass

	def placeWordInCrossword(self,board,word):
		"""
		The function to find the cross word can be placed vertically or horizontally

		"""

		self.board = board:
		self.row = len(self.board) -1 
		self.col = len(self.board[0]) -1 


		#star the board traversal 

		for i in range(self.row):

			for j in range(self.col) :

				if self.board[i][j] != "#":

					if self.helper_dfs(i,j,1) :

						return True


		return False




