"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""

"""
Input: grid = [[0,1],[1,0]]
Output: 2


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


"""


"""

apporach using a BFS 

traversal of grid 

start from top left to right bottom 

start(0,0) to (n-1,n-1)

can't go up ? 

we can move in 8 dirs 

with base case 

how will I know reached if (row,col) == (len(n)-1, len(n)-1)


#bfs 

queue = deque()

aslo the visited 

if grid[row][col] == 0: #then process
	
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1



"""
from typing import List

from collections import deque


class Solution():

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    	"""
		The function to find the shortest path in a grid 
    	"""

    	#constrinat case 
    	if len(grid) == 1 and len(grid[0]) == 1   :

    		return 0

    	#make the queue and put first position
    	queue = deque([(0,0)])

    	result = 0

    	dirs = [(-1,0),(-1,-1),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1)]

    	#start the itertation 
    	while queue :

    		row , col = queue.popleft()

    		for x_dir, y_dir in dirs:

    			new_x , new_y = row + x_dir , col + y_dir

    			if 0 <= new_x <= len(grid) - 1 and 0 <= new_y <= len(grid) - 1 and grid[new_x][new_y] == 0:

    				if new_x == len(grid) - 1  and new_y == len(grid) - 1 :

    					return result

    				queue.append([new_x, new_y])

    		result += 1

    	return -1  