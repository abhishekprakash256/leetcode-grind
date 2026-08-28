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

class SolutionWrong:

	def __init__(self):

		self.res = []
		self.board = []
		self.found = False


	def _make_board(self,n ):

		#make the row and col
		
		self.board = []

		for i in range(n):
			
			self.board.append(["."] * n)




	def _helper(self , x , y , dir  ):
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

		#travserse if the dir is not given
		if dir == "" :

			self._helper(x , y - 1 , "up")


			self._helper(x , y + 1 , "dowm")


			self._helper(x - 1, y  , "left" )


			self._helper(x + 1, y , "right" )
		

			self._helper(x -1 , y - 1, "up_left" )


			self._helper(x + 1 , y - 1, "up_right" )


			self._helper(x - 1 , y + 1, "down_left" )


			self._helper(x + 1 , y + 1, "down_right" )



		#travserse if the dir is given
		if dir == "up" :

			self._helper(x , y - 1 , "up")


		if dir == "dowm" :

			self._helper(x , y + 1 , "dowm")


		if dir == "left" :

			self._helper(x - 1, y  , "left" )


		if dir == "right" :

			self._helper(x + 1, y , "right" )


		if dir == "up_left" :

			self._helper(x -1 , y - 1, "up_left" )


		if dir == "up_right" :

			self._helper(x + 1 , y - 1, "up_right" )


		if dir == "down_left" :

			self._helper(x - 1 , y + 1, "down_left" )


		if dir == "down_right" :

			self._helper(x + 1 , y + 1, "down_right" )





	def solveNQueens(self, n: int) -> List[List[str]]:
		"""
		The function to find the N queens soln
		"""

		self.n = n

		#make the board
		self._make_board(n)

		#traverse the matrix
		
		for i in range(n):

			for j in range(n) :

				self._helper(i , j , "")








		
		



if __name__ == '__main__':

	sol = Solution()

	sol.solveNQueens(4)

	print(sol.board)




