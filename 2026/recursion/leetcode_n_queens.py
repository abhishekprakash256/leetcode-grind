"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""

"""

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]


"""



"""
approach -- 

queen can move, up , down , diagonally , till edge 

put the queen ?? 



"""



from typing import List

class Solution:

	def __init__(self):

		self.res = []
		self.board = []

	def _make_board(self,n ):

		#make the row and col
		row = ["."]*n
		self.board = []

		for i in range(n):

			self.board.append(row)




	def _helper(self):
		"""
		The helper function for the traversal
		"""







	def solveNQueens(self, n: int) -> List[List[str]]:
		"""
		The function to find the N queens soln
		"""

		#make the board
		self._make_board(n)

		#put the queen
		
		



if __name__ == '__main__':

	sol = Solution()

	sol.solveNQueens(4)

	print(sol.board)




