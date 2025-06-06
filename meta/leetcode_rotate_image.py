"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees
 (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.
"""

"""

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

"""

"""
approach -- 

 [[1,2,3],
  [4,5,6],
  [7,8,9]]


 [[7,4,1],
  [8,5,2],
  [9,6,3]]



make four pointers 
top_left , top_right , bottom_left , bottom_right

rows_len = len(matrix) - 1 
col_len = len(matrix) - 1

[0,0] , [0,col_len] , [row_len,col_len] , [col_len, 0 ]



"""

class Solution:
    """
    passes leet code 
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Iterate through each layer
        for layer in range(n // 2):  
            first, last = layer, n - 1 - layer  # Define the boundary of the layer
            for i in range(first, last):
                offset = i - first  # Position offset within the layer
                
                # Perform 4-way swap
                top = matrix[first][i]  # Store top element
                matrix[first][i] = matrix[last - offset][first]  # Left → Top
                matrix[last - offset][first] = matrix[last][last - offset]  # Bottom → Left
                matrix[last][last - offset] = matrix[i][last]  # Right → Bottom
                matrix[i][last] = top  # Top → Right




        

