"""
The word can be constructed from letters of sequentially adjacent cells,
 where adjacent cells are horizontally or vertically neighboring.
 The same letter cell may not be used more than once.
"""


"""
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

"""



"""
approach using a graph problem like DFS and search the grid and add the word in the unique list 

base case 
if len(serahc_list) > len(word) :

    return 

if len(search_list) == len(word) :

    if searc_lsit = list(word) :

        return True


make the grid as touched 

then add to the temp list with all dirs

run a dfs as per grid 


"""


from typing import List

class Solution_wrong:
    
    def _helper_dfs(self,i,j,search_lst):
        """
        The helper dfs to function to search the grdi
        """

        #base case 
        if i < 0 or i > self.row - 1 or j < 0 or j > self.col - 1  or self.board[i][j] == 0 :

            return

        if len(search_lst) > len(self.word) :

            return

        if len(search_lst) == len(self.word) :

            if search_lst == self.word :

                return True 

        #mark the grid
        temp = self.board[i][j]
        self.board[i][j] = 0 

        #traverse the grid
        up = self._helper_dfs(i , j - 1 , search_lst + [temp])
        down = self._helper_dfs(i, j +1 , search_lst + [temp])
        left = self._helper_dfs(i - 1, j , search_lst + [temp])
        right = self._helper_dfs(i + 1, j , search_lst + [temp] )

        if up or down or left or right :

            return True

        #revert the grid
        self.board[i][j] = temp

        return False



    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        The function to find the word exists in the board or not 
        """

        self.board = board
        self.word = list(word)

        self.row = len(self.board)
        self.col = len(self.board[0])


        #constraint case 
        if self.row == 1 and self.col == 1 :

            if self.board[0] == self.word :

                return True

        #make the call for dfs
        for i in range(self.row) :

            for j in range(self.col) :

                search_lst = [self.board[i][j]]

                if self._helper_dfs(i,j,search_lst) :

                    return True


        return False












class Solution_wrong2:

    def _helper_dfs(self,i,j,search_lst):
        """
        The helper dfs for the search of the word
        """

        #base case

        #bounds error 
        if i < 0 or i > self.row - 1 or j < 0 or j > self.col - 1 or self.board[i][j] == 0 :

            return
 
        #if the length is greater 
        if len(search_lst) > len(self.word) :

            return

        #length is equal
        if len(search_lst) == len(self.word) :

            if search_lst == self.word :

                return True

        #take the board value
        temp = self.board[i][j]
        self.board[i][j] = 0 

        #add the value in the list
        search_lst.append(temp)

        #make the recursive calls 
        left = self._helper_dfs(i-1,j,search_lst)
        right = self._helper_dfs(i,j+1, search_lst)
        up = self._helper_dfs(i,j-1, search_lst)
        down = self._helper_dfs(i,j+1,search_lst)

        #check for vals
        if left or right or up or down :

            return True

        #remove the value
        search_lst.pop()

        return False



    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        The function to make to find the word in the board
        """

        self.board = board
        self.word = list(word)

        self.row = len(self.board)
        self.col = len(self.board[0])

        #constraint case 
        if self.row == 1 and self.col == 1 :

            if self.board[0] == self.word :

                return True

        #make the helper function calls
        for i in range(self.row) :

            for j in range(self.col) :

                if self._helper_dfs(i,j,[]) :

                    return True

        return False




class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if self.dfs(i, j, 0):
                    return True
        return False

    def dfs(self, i, j, index):
        # Base cases
        if index == len(self.word):
            return True
        if (i < 0 or i >= self.rows or 
            j < 0 or j >= self.cols or 
            self.board[i][j] != self.word[index]):
            return False

        # Save current character and mark as visited
        temp = self.board[i][j]
        self.board[i][j] = '#'

        # Explore all directions
        found = (
            self.dfs(i+1, j, index+1) or
            self.dfs(i-1, j, index+1) or
            self.dfs(i, j+1, index+1) or
            self.dfs(i, j-1, index+1)
        )

        # Restore the original character
        self.board[i][j] = temp

        return found
