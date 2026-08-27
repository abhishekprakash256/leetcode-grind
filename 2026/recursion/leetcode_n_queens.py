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

traveral is -1,-1 
+1 , + 1
-1, +1 
+1 , -1 
-1 ,0 
0 , -1
+1 , 0 
0 , +1 


make a grid 

run one queen , mark all the postions can traverse 

find the vacant position and then put the other quen 


I have to also track the dir , if moving in one direction then can only move in that direction not anywhere else ?? 

pass the dir var and make the movement ??




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




	def _helper(self , x , y ):
		"""
		The helper function for the traversal
		"""

		#boundary case
		if x < 0 or y < 0 or x > self.n - 1 or y > self.n - 1 :

			return

		#bound case
		if self.board[x][y] == "#" :

			return


		#mark the board 
		#temp = self.board[x][y]

		self.board[x][y] = "#"


		#traverse the board 
		self._helper(x -1 , y - 1 )

		self._helper(x + 1 , y + 1 )

		self._helper(x - 1 , y + 1 )
		
		self._helper(x + 1 , y - 1 )

		self._helper(x -1 , y )

		self._helper(x , y -1 )

		self._helper(x + 1, y )

		self._helper(x , y + 1)	

		#unmark the board
		#self.board[x][y] = temp





	def solveNQueens(self, n: int) -> List[List[str]]:
		"""
		The function to find the N queens soln
		"""

		self.n = n

		#make the board
		self._make_board(n)

		#put the queen
		self._helper(0 , 0)






		
		



if __name__ == '__main__':

	sol = Solution()

	sol.solveNQueens(4)

	print(sol.board)




