"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton 
devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live 
(represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors
 (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously. Given the current state of the m x n grid board, 
return the next state.
"""




"""
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

"""



"""
[0,1,0]      [0,0,0]
[0,0,1]  ==> [1,0,1]
[1,1,1]      [0,1,1]
[0,0,0]      [0,1,0]


(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)


cor_set = ((-1,-1), (-1,0), (-1,+1) ,(0,-1),(0, +1) ,(+1,-1) , (+1,0), (+1,+1))

create a hash map

mapper = {}

for i in range(row_len):
    for j in range(col_len):
        
        if board[i][j] == 1:
            mapper{[[i],[j]]} = True


for cor in mapper:

    for cor_x, cor_y in cor_set:
        
        if (cor[0] - cor_x) < 0:
            pass







        
   


"""

