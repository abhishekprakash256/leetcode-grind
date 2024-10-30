"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

"""


"""

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


[1,2,3]    [7,2,1]    [7,4,1] 
[4,5,6]    [4,5,6]    [8,5,2]
[7,8,9]    [9,8,3]    [9,6,3]

[7,4,1]
[8,5,2]
[9,6,3]

"""

"""
l , r , lb, rb


l = [0][0]
r = [0][len(matrix[0]) - 1] 

lb = [len(matrix) - 1][0]
rb = [len(matrix) - 1][len(matrix[0]) - 1]


l = 0 
r = 0 

while l != r :

	for i in range(len(matrix)-1):
		
		temp = matrix[l][i]


"""


class Solution():
	def rotate(self,matrix):
		n = len(matrix)
		
		# Rotate each layer of the matrix
		for layer in range(n // 2):  # Only go halfway (layer by layer)
			first = layer
			last = n - layer - 1
			
			for i in range(first, last):
				# Offset is used to keep track of the current index within the layer
				offset = i - first
				
				# Save the top element
				top = matrix[first][i]
				
				# Move left to top
				matrix[first][i] = matrix[last - offset][first]
				
				# Move bottom to left
				matrix[last - offset][first] = matrix[last][last - offset]
				
				# Move right to bottom
				matrix[last][last - offset] = matrix[i][last]
				
				# Assign top to right
				matrix[i][last] = top
		
		return matrix
