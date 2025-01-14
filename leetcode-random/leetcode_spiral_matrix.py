"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

"""
example 1 - 
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

example 2 - 
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

"""
approach -- 

matix = [[1,2,3],[4,5,6],[7,8,9]]



"""


"""
appproach -- 

make 4 pointer 

top left = (0,0)
top right = (0, len(matrix)-1)
bottom left = (len(matrix)-1, 0 )
bottom right = (len(matrix)-1, len(matrix)-1)


movement = first row 

top_left = (0,0)

res_lst = []


while top_left != top_right or bottom_left != bottom_right :

	for i in range(top_left[1], top_right[1]) :

		res_lst.append(matrix[top_left[0]][i])


	for j in range(top_right[0], bott_right[0]) :

		res_lst.append(matrix[j][top_right[0]])


	for k in reverse(range(bottom_right[1], bottom_left[1])):

		res_lst.append(matrix[bottom_left[0]][k])



	for l in reverese(range(bottom_left[0], top_left[0]) :

		res_lst.append(matrix[l][bottom_left[1]])
		
	

	#make the pointer shift 
	
	top_left = (top_left[0] + 1, top_left[1] + 1)
	top_right = (top_right[0]+1, top_right[1] -1)
	bottom_left = (bottom_left[0] -1 , bottom_left[1] + 1)
	bottom_right = (bottom_right[0] -1 , bottom_right[1] -1 )








"""

class Solution:
    def spiralOrder(self, matrix):
        """
        The function to print the spiral matrix form.
        """

        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return []

        # Result list
        res_lst = []

        # Initialize the corners
        top_left = (0, 0)
        top_right = (0, len(matrix[0]) - 1)
        bottom_left = (len(matrix) - 1, 0)
        bottom_right = (len(matrix) - 1, len(matrix[0]) - 1)

        while top_left[0] <= bottom_left[0] and top_left[1] <= top_right[1]:
            # Traverse from top-left to top-right
            for i in range(top_left[1], top_right[1] + 1):
                res_lst.append(matrix[top_left[0]][i])

            # Traverse from top-right to bottom-right
            for i in range(top_right[0] + 1, bottom_right[0] + 1):
                res_lst.append(matrix[i][top_right[1]])

            # Traverse from bottom-right to bottom-left (if still within bounds)
            if top_left[0] < bottom_left[0]:
                for i in range(bottom_right[1] - 1, bottom_left[1] - 1, -1):
                    res_lst.append(matrix[bottom_left[0]][i])

            # Traverse from bottom-left to top-left (if still within bounds)
            if top_left[1] < top_right[1]:
                for i in range(bottom_left[0] - 1, top_left[0], -1):
                    res_lst.append(matrix[i][bottom_left[1]])

            # Move the corners inward
            top_left = (top_left[0] + 1, top_left[1] + 1)
            top_right = (top_right[0] + 1, top_right[1] - 1)
            bottom_left = (bottom_left[0] - 1, bottom_left[1] + 1)
            bottom_right = (bottom_right[0] - 1, bottom_right[1] - 1)

        return res_lst


