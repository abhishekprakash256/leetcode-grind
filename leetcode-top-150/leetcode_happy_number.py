"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle 
which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


"""
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 
"""

"""
hashmap to store values


and check for cycle 

if it gets 1 them store 

make as str to iter values and then int to calc the values 

"""



class Solution:
	def isHappy(self, n: int) -> bool:
		"""
		The function to make the hash map
		passes leetcode
		"""

		#base case 
		if n == 1 :
			return True 
		
		#hash map 
		mapper = {}

		#make the loop 
		n = str(n)

		#digit sum
		digit_sum = 0

		while True:

			for digit in n :

				digit = int(digit)

				digit_sum += digit*digit

			if digit_sum == 1:
				return True
			
			if digit_sum not in mapper:

				mapper[digit_sum] = True
			
			else:

				return False
			
			n = str(digit_sum)
			digit_sum = 0 





			

		