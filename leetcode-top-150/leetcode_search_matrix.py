"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

"""


"""
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104



"""


"""
approach -- 

using binary search -- 

in 2d 

1. 
make a empty list 
and add the rows like a list 
becmoes a linear list and run binary search 
use more memory 

2. 

use two pointer and jump the rows and col too 
how to change row and col ? 

mid = (i+len(nums))-1 // 2 , (j + len(nums)-1//2)

then boundary problem 

if mid[i] == len(nums[0]) - 1






"""

matrix = [
[1,3,5,7],
[10,11,16,20],
[23,30,34,60]
]

print(matrix[0][0])

print(matrix[(0+len(matrix)-1)//2][ (0 + len(matrix[0]))//2] )



class Solution():

	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		"""
		The function to search a 2d matrix using binary search
		"""

		#constraints 
		if len(matrix) == 1 and len(matrix[0]) == 1 :

			if matrix[0][0] == target :

				return True

			else:

				return False


		#start the traversal 
		a , b = 0 , 0
		c , d  = len(matrix) - 1, len(matrix[0]) - 1 


		#start the loop 
		while a <= c and b <= d :

			mid1 , mid2 = (a+c)//2 , (b+d)//2

			if matrix[mid1][mid2] == target :

				return True


			elif target < matrix[mid1][mid2] :

				#right shit before mid

				if mid2 == 0 :

					mid1 = mid1-1
					mid2 = len(matrix[0]) - 1

					c = mid1
					d = mid2

				else:

					c = mid1
					d = mid2 - 1 



			else:

				#left shift after the mid 

				if mid2 == len(matrix[0]) - 1 :

					mid1 = mid1 + 1 
					mid2 = 0 

					a = mid1
					b = mid2

				else:

					a = mid1
					b = mid2 + 1 




		return False 



























