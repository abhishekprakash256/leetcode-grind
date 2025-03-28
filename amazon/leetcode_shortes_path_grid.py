"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) 
to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles.
If it is not possible to find such walk return -1.
"""

"""
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""



"""

shortest path , must be bfs 

remove obstacle 

can remove and can not 

the calcluate the number of moves and keep the min moves 

if found the last point then get the moves 

a recursive decision tree for that ? 


"""
from typing import List

from collections import deque


class Solution():

	def __init__(self):

		self.min_steps = 0


    def shortestPath(self, grid: List[List[int]], k: int) -> int:
    	"""
    	Find the shortest solution in grid
    	"""

    	#constraint case 
    	if len(grid) == 1 and len(grid[0]) == 1 :

    		if grid[0] == 1 and k >= 1 :

    			return 1 

    		elif grid[0] == 0 :

    			return 1 

    		else :

    			return 0

    	#dims 
    	rows = len(grid) - 1 
    	cols = len(grid[0]) - 1

    	#make the traversal dirs
    	dirs = [[-1,0], [1,0], [0,-1],[0,1]]

    	#queue for points
    	queue = deque([0,0])

    	steps = 1 

    	#visted points 
    	visted = set()

    	#start the traversal 
    	while 







