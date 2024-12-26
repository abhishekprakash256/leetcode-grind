"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not 
be used more than once.
"""

"""
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true



Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.




"""


class Solution():
	"""
	Slower solution
	"""

	def helper_dfs(self,i,j,res_lst):
		"""
		The function to make the dfs of the word grid
		"""

		#check for the word
		if res_lst == self.word :

			return True
			
		#base case 
		if i < 0 or j < 0 or i > len(self.board)-1 or j > len(self.board[0])-1 or self.board[i][j] == "#" :

			return 


		#temprory mark the board
		temp = self.board[i][j]
		self.board[i][j] = "#"

		#start the dfs search


		found = (
			self.helper_dfs(i-1,j,res_lst + [temp]) or 
			self.helper_dfs(i+1,j,res_lst + [temp]) or 
			self.helper_dfs(i,j-1,res_lst + [temp]) or 
			self.helper_dfs(i,j+1,res_lst + [temp])
			)



		self.board[i][j] = temp

		return found




	def exist(self,board,word):
		"""
		The function to search the board
		"""

		self.board = board
		self.word = list(word)

		#constraints 
		if len(self.board) == 1 and len(self.board[0]) == 1 and self.board[0] == self.word:

			return True


		#start the dfs recursion 
		for i in range(len(self.board)) :

			for j in range(len(self.board[0])) :

				if self.board[i][j] == self.word[0] :

					if self.board[i][j] != "#":

						if self.helper_dfs(i,j,[]) :

							return True


		return False





if __name__ == '__main__':
	sol = Solution()
	print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))


