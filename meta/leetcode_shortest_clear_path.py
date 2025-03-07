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
    """
    passes leetcode
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        The function to find the shortest path in a grid 
        """

        #constrinat case 

        #the grid is one length
        n = len(grid) - 1

        # Edge cases
        if grid[0][0] == 1 or grid[n][n] == 1:
            return -1

        #the grid has (0,0) as 1
        # If it's a 1x1 grid and the only cell is 0
        if n == 0:

            return 1

        #make the queue and put first position
        queue = deque([(0,0,1)])

        #make the visited set
        visited = set([(0,0)])

        dirs = [(-1,0),(-1,-1),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1)]

        #start the itertation 
        while queue :

            row , col , result = queue.popleft()

            for x_dir, y_dir in dirs:

                new_x , new_y  = row + x_dir , col + y_dir

                if 0 <= new_x <= n and 0 <= new_y <= n and grid[new_x][new_y] == 0 and (new_x,new_y) not in visited:

                    if new_x == n and new_y == n :

                        return result + 1 

                    visited.add((new_x,new_y))

                    queue.append((new_x, new_y, result + 1 ))

        return -1  




class Solution_two_loop():
    """
    passes leetcode
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        The function to find the shortest path in a grid 
        """

        #constrinat case 

        #the grid is one length
        n = len(grid) - 1

        # Edge cases
        if grid[0][0] == 1 or grid[n][n] == 1:
            return -1

        #the grid has (0,0) as 1
        # If it's a 1x1 grid and the only cell is 0
        if n == 0:

            return 1

        #make the queue and put first position
        queue = deque([(0,0)])

        #make the visited set
        visited = set([(0,0)])

        #result 
        result = 1 

        dirs = [(-1,0),(-1,-1),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1)]

        #start the itertation 
        while queue :

            length_queue = len(queue)

            for _ in range(length_queue) :

                row , col , result = queue.popleft()

                for x_dir, y_dir in dirs:

                    new_x , new_y  = row + x_dir , col + y_dir

                    if 0 <= new_x <= n and 0 <= new_y <= n and grid[new_x][new_y] == 0 and (new_x,new_y) not in visited:

                        if new_x == n and new_y == n :

                            return result + 1 

                        visited.add((new_x,new_y))

                        queue.append((new_x, new_y))

            result += 1

        return -1  