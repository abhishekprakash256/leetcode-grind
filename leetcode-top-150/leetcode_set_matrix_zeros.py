"""

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


"""
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


"""



"""
[1,1,1]
[1,0,1]
[1,1,1]


[1,0,1]
[0,0,0]
[1,0,1]

put the zeros location in the set

row_set = ()

col_set = ()

iterate the set to make them zero either row or col 

"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        passes leetcode
        """
        #base case
        if not matrix:
            return None


        #make the sets 
        row_set = set()
        col_set = set()

        #get the length
        row_len = len(matrix)
        col_len = len(matrix[0])


        #start the loop for getting zeros
        for i in range(row_len):

            for j in range(col_len):

                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)


        
        #make the row zeros 
        for i in row_set:

            for j in range(col_len):

                matrix[i][j] = 0
        
        #make the col zeros 
        for i in col_set:

            for j in range(row_len):

                matrix[j][i] = 0
        
        return None 


        
