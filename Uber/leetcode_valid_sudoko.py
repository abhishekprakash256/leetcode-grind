"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


"""


"""

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.


"""



"""
approach --

The algo is very simple check the condn one by one 

use a dict to check to go around the rows and store the vals 

use a dict for the cols store values and check 

use a dict for the 3X3 block 

start point array 

and then make the array move 3 X 3 


[0,0], [0,3] [0,6]

3,0 , [3,3] [3,6]

[6,0] [6,3] , [6,6]
"""


class Solution:
    """
    passese leetcode
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        The function to check the valid sudoku
        """

        row = 9
        col = 9 

        #traverse the rows

        for i in range(row) :

            row_mapper = {}

            for j in range(col) :

                if board[i][j] == "." :

                    continue

                else :

                    if board[i][j] in row_mapper :

                        return False

                    row_mapper[board[i][j]] = True



        #traverse the col 
        for i in range(row) :

            col_mapper = {}

            for j in range(col) :


                if board[j][i] == "." :

                    continue

                else :

                    if board[j][i] in col_mapper :

                        return False

                    col_mapper[board[j][i]] = True


        points = [[0,0] ,[0,3] ,[0,6] ,[3,0] ,[3,3] , [3,6] , [6,0] ,[6,3] ,[6,6]]

        #traverese the 3 X 3 block

        for x,y in points :

            block_mapper = {}

            for i in range(x,x+3) :

                for j in range(y,y+3) :

                    if board[i][j] == "." :

                        continue

                    else :

                        if board[i][j] in block_mapper :

                            return False

                        block_mapper[board[i][j]] = True


        return True






















