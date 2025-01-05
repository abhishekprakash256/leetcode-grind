"""
Given an integer x, return true if x is a
palindrome , and false otherwise.

"""

"""

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1


"""


"""
appraoch --

using two pointer 

edge case if -ve return false

covert to str 

and match the value with two ptr

"""



class Solution():

	def isPalindrome(self,x) :
		"""
		The function to find a pallindrome number
		passes leetcode
		
		"""

		#constarint
		if x < 0 :

			return False

		#convert to str
		x = str(x)

		#initilaize the ptr
		l , r = 0, len(x) - 1

		while l < r :

			if x[l] != x[r] :

				return False

			l += 1 
			r -= 1


		return True







