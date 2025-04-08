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

if the list matches we rerturn true 

and the movement will be marked by # as they are explored 





"""