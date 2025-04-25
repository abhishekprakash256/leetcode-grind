"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""


"""
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1


"""

"""

approach -- 

take the point and travers all the possible path 

keep the count as per point 

if increasing keep the count up 

if decreasing update the max count with curr count 

we can use dfs strategy for the traversal 

and mark the visited by tmp then unmark again 

for the base case we can keep the bounds and marking 



"""
from typing import List

class Solution_Worng:

    def __init__(self):

        self.max_count = 0


    def _helper_dfs(self,i,j,count) :
        """
        The function to traverse the graph using dfs
        """

        #base case 
        if i < 0 or i > self.row or j < 0 or j > self.col or self.matrix[i][j] == "#" :

            return

        #not increasing case
        if self.matrix[i][j] > self.matrix[i-1][j] or self.matrix[i][j] > self.matrix[i+1][j] or self.matrix[i][j] > self.matrix[i][j-1] or self.matrix[i][j] > self.matrix[i][j+1] :

            return 

        #increase the count case 
        count += 1 

        #mark the graph
        temp = self.matrix[i][j]
        self.matrix[i][i] = "#"

        #traverse the graph
        up = self._helper_dfs(i, j-1, count)
        down = self._helper_dfs(i, j+1 , count)
        left = self._helper_dfs(i-1 , j, count)
        right = self._helper_dfs(i+1 , j, count)

        self.max_count = max(self.max_count, count)

        #unmark the matrix
        self.matrix[i][j] = temp





    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        The function to find the longest increasing sequence in matix
        """

        self.matrix = matrix
        self.row = len(self.matrix)
        self.col = len(self.matrix[0])


        #constraint case 
        if self.row == 1 and self.col == 1 :

            return 1

        #traverse the matrix 
        for i in range(self.row) :

            for j in range(self.col) :

                count = 0 

                self._helper_dfs(i,j, count)


        return self.max_count  






class Solution_gpt:

    def __init__(self):
        self.max_count = 0
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def _helper_dfs(self, i, j, dp):
        # If already computed, return memoized result
        if dp[i][j] != -1:
            return dp[i][j]

        max_len = 1  # At least the cell itself

        for dx, dy in self.directions:
            x, y = i + dx, j + dy

            if 0 <= x < self.row and 0 <= y < self.col and self.matrix[x][y] > self.matrix[i][j]:
                length = 1 + self._helper_dfs(x, y, dp)
                max_len = max(max_len, length)

        dp[i][j] = max_len
        return max_len

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        dp = [[-1 for _ in range(self.col)] for _ in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):
                self.max_count = max(self.max_count, self._helper_dfs(i, j, dp))

        return self.max_count



class Solution():

    def __init__(self):

        self.max_count = 0
        self.directions = [[-1,0], [1,0],[0,-1],[0,1]]


    def _helper_dfs(self,i,j,count):
        """
        The function to traverse the matrix in dfs
        """

        #base case 

        if i < 0 or i > self.row - 1 or j < 0 or j > self.col - 1 or self.matrix[i][j] == "#" :

            return

        #mark the matrix
        temp = self.matrix[i][j]

        self.matrix[i][j] = "#"

        for dx, dy in self.directions :

            new_x , new_y = i + dx , j + dy

            #check the condn 

            if 0 <= new_x <= self.row - 1 and 0 <= new_y <= self.col - 1 and self.matrix[i][j] < self.matrix[new_x][new_y] :

                count += 1

                self.matrix[i][j] = temp

                self._helper_dfs(new_x , new_y , count)
                        
                self.max_count = max(self.max_count , count)


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        The function to find the longest increasing sequence in the matrix
        """

        self.matrix = matrix
        self.row = len(self.matrix)
        self.col = len(self.matrix[0])


        #constraint case 
        if not self.matrix or len(self.matrix) == 1:

            return 0 

        #traverese the matrix
        for i in range(self.row) :

            for j in range(self.col) :

                count = 0

                self._helper_dfs(i, j , count)

        return self.max_count 


















































































