"""
find the number of the islands in a given grid 

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by 

connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""




"""

algo -- 

take a point i,j
traverse a dfs and visited and make it zero 

and increase count += 1

keep the bound to check for all the borders
"""




grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

class Solution():


    def dfs(self,grid,i,j):
        """
        The dfs search for the finding of the island 
        """
        #make the boud
        
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == "0":
            return None 
        
        grid[i][j] = "0"
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
    
    def numIslands(self,grid):
        """
        The function to find th number of the islands 
        """
        #base case 
        if len(grid) == 0 or len(grid[0]) == 0 : 
            return None

        
        #traverse the grid 
        rows = len(grid)
        columns = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    count +=1
                
                self.dfs(grid,i,j)
        
        return count



if __name__ == "__main__":
    sol = Solution()

    res = sol.numIslands(grid)

    print(res)

