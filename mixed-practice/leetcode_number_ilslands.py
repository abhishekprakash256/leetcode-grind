"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

"""


"""

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.



"""




from collections import deque

class Solution_dfs():
    """
    passes leetcode
    """

    def __init__(self):

        self.count = 0

    def helper_dfs(self,i,j):
        """
        The function to do the dfs traversal for the grid
        """

        #base case 
        if i < 0 or j < 0 or i > self.row - 1 or j > self.col - 1  or self.grid[i][j] == "0":

            return

        #make the grid "0"
        self.grid[i][j] = "0"

        #make the recursive call
        up = self.helper_dfs(i-1,j)
        down = self.helper_dfs(i+1,j)
        left = self.helper_dfs(i,j-1)
        right = self.helper_dfs(i,j+1)



    def numIslands(self,grid):
        """
        The function to find the number of the islands in the grid 
        """

        #make the vars
        self.grid = grid

        self.row = len(self.grid)
        self.col = len(self.grid[0])

        #iterate the rows and the cols 
        for i in range(self.row) :

            for j in range(self.col) :

                if self.grid[i][j] == "1" :

                    self.count += 1 

                self.helper_dfs(i,j)

        return self.count



class Solution():
    """
    The solution using bfs 
    """

    def __init__(self):

        self.count = 0

    def helper_bfs(self,i,j) :
        """
        The helper function to do bfs
        """
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] #the possible 

        queue = deque([(i,j)])

        #make the mark
        self.grid[i][j] = "0"

        while queue :

            #pop the queue
            x, y = queue.popleft()

            #traverse all the dirs
            for dx , dy in dirs :

                nx , ny = x + dx , y + dy

                #make the bound conditio
                if 0 <= nx <= self.row - 1 and 0 <= ny <= self.col - 1 and self.grid[nx][ny] == "1" :

                    #mark as visited
                    self.grid[nx][ny] = "0"

                    #append to queue 
                    queue.append((nx,ny))



    def numIslands(self,grid) :
        """
        The function to find the number of island in grids
        """

        self.grid = grid
        self.row = len(self.grid)
        self.col = len(self.grid[0])


        #constarint case
        if self.row == 1 and self.col == 1 :

            if self.grid[0][0] == "1" :

                return 1

            else :

                return 0

        #make the taveral 
        for i in range(self.row) :

            for j in range(self.col) :

                #find the grid value that is 1
                if self.grid[i][j] == "1" :

                    self.count += 1 

                    self.helper_bfs(i,j)


        return self.count





class Solution():

    def numIslands(self,grid):
        """
        The function to find the number of the islands
        passes leetcode
        """

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        #constarint case
        if rows == 1 and cols == 1 :

            if grid[0][0] == "1" :

                return 1

            else :

                return 0

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] #the possible

        #make the queue
        #queue = deque()

        #make the loop over the points 
        for i in range(rows) :

            for j in range(cols) :

                if grid[i][j] == "1" :

                    count += 1

                    #append the value in the queue
                    queue = deque([(i,j)])

                    #start the loop over the queue
                    while queue :

                        x , y = queue.popleft()

                        for dx, dy in dirs :

                            nx , ny = x + dx , y + dy 

                            #make the bound conditio
                            if 0 <= nx <= rows - 1 and 0 <= ny <= cols - 1 and grid[nx][ny] == "1" :

                                #mark the grid
                                grid[nx][ny] = "0"

                                queue.append((nx,ny))

        return count





























        

