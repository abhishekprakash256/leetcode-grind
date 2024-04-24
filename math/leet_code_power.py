"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Input: x = 2.00000, n = 10
Output: 1024.00000
"""


class Solution():

	def myPow(self,x,n):
		"""
		The function to find the power of the number
		"""

		#base case 
		if n == 0:
			return 1 

		elif n > 0 :

			val = 1

			for i in range(n):
				val = val*n



