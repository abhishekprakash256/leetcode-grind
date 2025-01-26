"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is 
impossible, return -1.

"""


"""
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.



"""


"""

0 - empty 
1 - fesh 
2 - rotten 

4 direction adjacent becomes rotten 
every minute 

adjacent becmoes rotten

return mimmun minute no oarnage ramon fresh

grid =  

if not possible return false 

minute = 0 

approach use a dfs algo --

dfs 

make the grid[i][j] = 2

count += 1 

two pass 

if grid[i][j] == 2 :

    helper_dfs(i,j)

other pass 

for i in 
    for j in 

        if grid[i][j] == 1 :

            return -1
            
return count

"""


#inputs 
grid1 = [[2,1,1],[1,1,0],[0,1,1]]

grid2 = [[2,1,1],[0,1,1],[1,0,1]]

grid3 = [[2,1,1],[1,1,1],[0,1,2]]



class Solution_wrong():
    """
    The solution is wrong and should use a DFS solution

    """

    def __init__(self):

        self.minutes = 0


    def helper_dfs(self,i,j):
        """
        The function to help the dfs traversal in the grid 
        """

        #base case

        #out of boud case and empoty and rotten case
        if i < 0 or j < 0 or i > self.row - 1 or j > self.col - 1 or self.grid[i][j] == 0 or self.grid[i][j] == "#":

            return None

        #mark the grid touched or make it rotten
        self.grid[i][j] = "#"

        #do the recursive call
        up = self.helper_dfs(i-1,j) 
        down = self.helper_dfs(i+1,j)
        left = self.helper_dfs(i,j-1)
        right = self.helper_dfs(i,j+1)

        if up or down or left or right :

            #increase the minutes
            self.minutes += 1

        return True



    def orangesRotting(self, grid):
        """
        The function to find the rotten oragne in the grid
        """

        #make the vars
        self.grid = grid
        self.row = len(self.grid)
        self.col = len(self.grid[0])

        #constarint case
        if self.row == 1 and self.col == 1 :

            if self.grid[0][0] == 2 or self.grid[0][0] == 0:

                return 0

            else:

                return -1


        #make the first pass for check the rotten oranges
        for i in range(self.row) :

            for j in range(self.col) :

                #print(i,j)

                if self.grid[i][j] == 2 :

                    self.helper_dfs(i,j)


        #print(self.grid)


        #check if any orange is remain ,i.e 1
        for i in range(self.row) :

            for j in range(self.col) :

                if self.grid[i][j] == 1 :

                    return -1


        #return the count
        return self.minutes





class Solution_wrong2():
    """
    The solution is wrong and should use a DFS solution

    """

    def __init__(self):

        self.minutes = 0


    def helper_dfs(self,i,j,time):
        """
        The function to help the dfs traversal in the grid 
        """

        #base case

        #out of boud case and empoty and rotten case
        if i < 0 or j < 0 or i > self.row - 1 or j > self.col - 1 or self.grid[i][j] == 0 or self.grid[i][j] == "#":

            return None

        #mark the grid touched or make it rotten
        self.grid[i][j] = "#"

        #make the time 
        self.minutes = max(self.minutes, time)

        #do the recursive call
        up = self.helper_dfs(i-1,j , time + 1 ) 
        down = self.helper_dfs(i+1,j, time + 1 )
        left = self.helper_dfs(i,j-1, time + 1 )
        right = self.helper_dfs(i,j+1, time + 1 )



    def orangesRotting(self, grid):
        """
        The function to find the rotten oragne in the grid
        """

        #make the vars
        self.grid = grid
        self.row = len(self.grid)
        self.col = len(self.grid[0])
        fresh_oranges = 0 

        #constarint case
        if self.row == 1 and self.col == 1 :

            if self.grid[0][0] == 2 or self.grid[0][0] == 0:

                return 0

            else:

                return -1

        # Count fresh oranges
        for i in range(self.row):

            for j in range(self.col):

                if self.grid[i][j] == 1:

                    fresh_oranges += 1



        #make the first pass for check the rotten oranges
        for i in range(self.row) :

            for j in range(self.col) :

                #print(i,j)

                if self.grid[i][j] == 2 :

                    self.helper_dfs(i,j,0)


        print(self.grid)


        #check if any orange is remain ,i.e 1
        for i in range(self.row) :

            for j in range(self.col) :

                if self.grid[i][j] == 1 :

                    return -1

        #return the count
        return self.minutes if fresh_oranges > 0 else 0





from collections import deque


class Solution_wrong3():

    def __init__(self):

        self.minutes = -1 


    def helper_bfs(self,i,j):
        """
        The function to traverse using bfs strategy
        """

        #make the dirs
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] #the possible 

        queue = deque([(i,j)])

        #print(queue)

        #make the mark
        self.grid[i][j] = 2

        #traverse the queue
        while queue :

            x , y = queue.popleft()

            for dx , dy in dirs :

                nx , ny = x + dx , y + dy 

                if 0 <= nx <= self.row - 1 and 0 <= ny <= self.col - 1 and self.grid[nx][ny] == 1 :

                    #mark the grid 
                    self.grid[nx][ny] = 2

                    #increase the minutes

                    #append in the queue for traversal
                    queue.append((nx,ny))

            if queue :

                self.minutes += 1


        


    def orangesRotting(self,grid) :
        """
        The function to get the minute for rotten orange
        """

        #make the vars
        self.grid = grid
        self.row = len(self.grid)
        self.col = len(self.grid[0])
        fresh_oranges = 0 

        #constarint case
        if self.row == 1 and self.col == 1 :

            if self.grid[0][0] == 2 or self.grid[0][0] == 0:

                return 0

            else:

                return -1

        #make the first pass for check the rotten oranges
        for i in range(self.row) :

            for j in range(self.col) :

                #print(i,j)

                if self.grid[i][j] == 2 :

                    self.helper_bfs(i,j)

        #print(self.grid)

        #check if any orange is remain ,i.e 1
        for i in range(self.row) :

            for j in range(self.col) :

                if self.grid[i][j] == 1 :

                    return -1


        return self.minutes




class Solution_wrong():

    def orangesRotting(self, grid):
        """
        The function to check for the rotten tomataoes and  time it takes
        """

        #get the row and cols
        rows = len(grid)
        cols = len(grid[0])
        minutes = -1


        #constarint case
        if rows == 1 and cols == 1 :

            if grid[0][0] == 2 or grid[0][0] == 0:

                return 0

            else:

                return -1

        #make the dirs
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] #the possible 

        #make the queue
        queue = deque()

        #add all the ornages position in the queue
        for i in range(rows) :

            for j in range(cols):

                if grid[i][j] == 2 :

                    queue.append((i,j))

        #start the traversal from the queue
        while queue :

            x, y = queue.popleft()

            #traverse the neighbor 
            for dx , dy in dirs :

                nx , ny = x + dx , y + dy

                #condn for the bound 
                if 0 <= nx <= rows - 1 and 0 <= ny <= cols - 1 and grid[nx][ny] == 1 :

                    #mark the grid
                    grid[nx][ny] = 2

                    queue.append((nx,ny))

            minutes += 1


        #check if any orange is there
        for i in range(rows) :

            for j in range(cols) :

                if grid[i][j] == 1:

                    return -1


        return minutes






class Solution:
    def orangesRotting(self, grid):
        """
        The function to check for the time it takes for all oranges to rot.
        passes leetcode
        """

        # Get the number of rows and columns
        rows = len(grid)
        cols = len(grid[0])

        # Initialize variables
        queue = deque()
        fresh_oranges = 0
        minutes = 0

        # Add all rotten oranges to the queue and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        # Directions for the neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Perform BFS
        while queue and fresh_oranges > 0:
            # Process all oranges at the current time step
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # If the neighbor is a fresh orange, rot it
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        queue.append((nx, ny))

            # Increment minutes after processing one level of BFS
            minutes += 1

        # If there are still fresh oranges, return -1
        return minutes if fresh_oranges == 0 else -1









































#sol = Solution()

#print(sol.orangesRotting(grid1))





