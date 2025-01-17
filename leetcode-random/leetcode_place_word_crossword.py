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


class Solution_wrong():

	def helper_dfs(self,i,j, count):
		"""
		The helper function to do the dfs 
		"""
		#make the base case :

		#the result case:
		if count == len(self.word) :

			return True


		#out of bound case
		if i < 0 or j < 0 or i >= self.row or j >= self.col or self.board[i][j] == "#":

			return

		#mark the board
		temp = self.board[i][j]
		self.board[i][j] = "#"

		#make the recursisve call
		up = self.helper_dfs(i-1,j, count +1 )
		down = self.helper_dfs(i+1,j, count + 1 )
		left = self.helper_dfs(i,j-1 , count + 1)
		right = self.helper_dfs(i,j+1 , count + 1 )


		#restore the board
		self.board[i][j] = temp

		return False





	def placeWordInCrossword(self,board,word):
		"""
		The function to find the cross word can be placed vertically or horizontally

		"""
		self.word = word
		self.board = board
		self.row = len(self.board) 
		self.col = len(self.board[0])


		#star the board traversal 

		for i in range(self.row):

			for j in range(self.col) :

				if self.board[i][j] != "#":

					if self.helper_dfs(i,j,1) :

						return True


		return False






class Solution_wrong():

	def helper_dfs(self,i,j,count,dir):
		"""
		The function to do the dfs traversal
		"""
		#make the base case 
		print(i,j)
		if i < 0 or j < 0 or i > self.row  or j > self.col  or self.board[i][j] == "#":

			return False



		#if matches 
		if count == len(self.word) :

			#print("in")

			if dir == "up" and ( (i - 1 ) < 0 or self.board[i-1][j] == "#") :

				return True

			elif dir == "down" and ( (i + 1 ) == self.row - 1 or self.board[i+1][j] == "#"):

				return True


			elif dir == "left" and ( (j - 1 ) < 0 or self.board[i][j-1] == "#") :

				return True

			elif dir == "right" and ( (j+1) == self.col - 1 or self.board[i][j+1] == "#" ):
				return True


		# Check if the current character matches or is a blank space.
		if self.board[i][j] != self.word[count] and self.board[i][j] != " ":

			return False

		#mark the board
		temp = self.board[i][j]
		self.board[i][j] = "#"

		#make the recursive call

		if dir == "up" :

			print("up")

			res = self.helper_dfs(i-1,j, count + 1, "up")

		elif dir == "down" :

			print("down")

			res = self.helper_dfs(i+1,j,count +1 , "down")

		elif dir == "left" :

			print("left")

			res = self.helper_dfs(i,j-1, count + 1 ,"left")

		elif dir == "right" :

			print("right")

			res = self.helper_dfs(i,j + 1, count + 1 , "right") 


		else :

			res = False


		#revert the board back 
		self.board[i][j] = temp

		return res 




	def placeWordInCrossword(self,board, word):
		"""
		The main function to find if we can make the cross word
		"""

		self.board = board
		self.word = word
		self.row = len(self.board)
		self.col = len(self.board[0])


		#make the dfs calls

		for i in range(self.row) :

			for j in range(self.col) :

				if self.word[0] == self.board[i][j] or self.word[len(word)-1] == self.board[i][j] or self.board == " " :

					if self.helper_dfs(i,j,1,"up") or self.helper_dfs(i,j,1,"down") or self.helper_dfs(i,j,1,"left") or self.helper_dfs(i,j,1,"right") :

						return True


		return False





class Solution():

	def helper_dfs(self,i,j,count,dir) :
		"""
		The function to make the helper dfs

		"""

		#print(i,j)

		#make the base case 
		if i < 0 or j < 0 or i > self.row - 1 or j > self.col - 1 or self.board[i][j] == "#" or self.board[i][j] not in (self.word[count], " ") :

			return False


		#make the equal case 
		if count == len(self.word) -1 :

			if dir == "up" and (i == 0 or self.board[i-1][j] == "#" ) :

				return True

			elif dir == "down" and ( i == self.row - 1 or self.board[i+1][j] == "#") :

				return  True

			elif dir == "left" and ( j == 0 or self.board[i][j-1] == "#") :

				return  True

			elif dir == "right" and ( j == self.col -1  or self.board[i][j+1] == "#") :

				return True


			return False


		#mark the postion 

		temp = self.board[i][j]
		self.board[i][j] = "#"


		#do the recursion call
		if dir == "up" :

			res = self.helper_dfs(i-1,j,count + 1, "up")

		elif dir == "down" :

			res = self.helper_dfs(i+1,j,count + 1, "down")

		elif dir == "left" :

			res = self.helper_dfs(i,j-1, count + 1 , "left")

		elif dir == "right" :

			res = self.helper_dfs(i,j+1, count + 1 ,"right")


		#revert the marking back
		self.board[i][j] = temp

		return res



	def placeWordInCrossword(self,board, word ) :
		"""
		The function to find the cross word can be set in the board
		"""

		self.board = board
		self.word = word
		self.row = len(self.board)
		self.col = len(self.board[0])

		#iterate the board
		for i in range(self.row) :

			for j in range(self.col) :

				if self.board[i][j] in (self.word[0], self.word[-1], " ") :

					if self.helper_dfs(i,j,0,"up") or self.helper_dfs(i,j,0,"down") or self.helper_dfs(i,j,0,"left") or self.helper_dfs(i,j,0,"right") :

						return True

		return False





class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = { 'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0) }

        def coord_is_start(r, c, dir):
            if board[r][c] == '#': return False
            if dir == 'down' and r-1 >= 0 and (board[r-1][c] == ' ' or board[r-1][c].isalpha()): return False
            if dir == 'right' and c-1 >= 0 and (board[r][c-1] == ' ' or board[r][c-1].isalpha()): return False
            if dir == 'up' and r+1 < rows and (board[r+1][c] == ' ' or board[r+1][c].isalpha()): return False
            if dir == 'left' and c+1 < cols and (board[r][c+1] == ' ' or board[r][c+1].isalpha()): return False
            return True

        def coord_is_end(r, c, dir):
            if dir == 'down' and (r+1 == rows or board[r+1][c] == '#'): return True
            if dir == 'right' and (c+1 == cols or board[r][c+1] == '#'): return True
            if dir == 'up' and (r-1 < 0 or board[r-1][c] == '#'): return True
            if dir == 'left' and (c-1 < 0 or board[r][c-1] == '#'): return True
            return False

        def dfs(r, c, dir):
            stack = [(r, c, 0)]
            while stack:
                i, j, l = stack.pop()
                if l+1 == len(word) and coord_is_end(i, j, dir): return True
                a, b = dirs[dir]
                ii, jj = i + a, j + b
                if 0 <= ii < rows and 0 <= jj < cols and l+1 < len(word) and (board[ii][jj] == word[l+1] or board[ii][jj] == ' '):
                    stack.append((ii, jj, l+1))
            return False

        for r in range(rows):
            for c in range(cols):
                for dir in dirs:
                    if coord_is_start(r, c, dir) and (board[r][c] == ' ' or board[r][c] == word[0]) and dfs(r, c, dir): return True

        return False










sol = Solution()

board = [["#"," ","#"],[" "," ","#"],["#","c"," "]]
word = "abc"

#out = True

res = sol.placeWordInCrossword(board,word)

print(res)