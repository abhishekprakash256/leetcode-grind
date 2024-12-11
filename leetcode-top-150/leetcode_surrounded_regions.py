"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

	Connect: A cell is connected to adjacent cells horizontally or vertically.
	Region: To form a region connect every 'O' cell.
	Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.

A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.


"""


"""

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]



Input: board = [["X"]]

Output: [["X"]]



"""


"""
approach -- 

use a dfs search on each point and then check and return True

base case
if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1
	return False

if grid[i][j] == "X" :
	
	return True 


if self.dfs(i-1,j) and self.dfs(i+1,j) and self.dfs(i,j-1) and  self.dfs(i,j-1) :
	grid[i][j] = "X"




"""


inp = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]




class Solution:
    def dfs(self, i, j):
        """
        The DFS function to mark boundary-connected 'O' regions.
        """
        # Base case: out of bounds or cell is not 'O'
        if i < 0 or j < 0 or i > self.row -1  or j > self.col -1  or self.board[i][j] != "O":
            return
        
        # Mark the cell as 'T' (temporary mark)
        self.board[i][j] = "T"
        
        # Traverse in all four directions
        self.dfs(i - 1, j)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i, j + 1)

    def solve(self, board) -> None:
        """
        Modify the board in-place to capture surrounded regions.
        passes leetcode
        """
        self.board = board

        # Base case: empty board
        if not board or not board[0]:
            return

        # Get the number of rows and columns
        self.row = len(board)
        self.col = len(board[0])


        # Step 1: Mark all boundary-connected 'O' regions with 'T'
        for i in range(self.row):
            if board[i][0] == "O":
                self.dfs(i, 0)
            if board[i][self.col - 1] == "O":
                self.dfs(i, self.col - 1)


        for j in range(self.col):
            if board[0][j] == "O":
                self.dfs(0, j)
            if board[self.row - 1][j] == "O":
                self.dfs(self.row - 1, j)


        # Step 2: Replace all remaining 'O' with 'X', and revert 'T' back to 'O'
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
















if __name__ == '__main__':
	sol = Solution()

	sol.solve(inp)









