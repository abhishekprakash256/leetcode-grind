"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith

digit of the integer. 

The digits are ordered from most significant to least significant in left-to-right order. 

The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

"""


"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.


"""


"""
approach -

reverse iteration 

carry = 1 

res_lst = []

val = nums[i] + carry

val = val % 10  

carry = val // 10 



"""


class Solution():

	def plusOne(self,digits):
		"""
		The function to plus one in the number
		passes leetcode
		"""

		#make the carry 
		carry =  1

		#make the iter
		i = len(digits) - 1 

		#make the sum lst
		res_lst = []

		while i >= 0 :

			val = digits[i] + carry

			carry = val // 10 

			val = val % 10 

			res_lst.append(val)

			i -= 1 



		#append if carry is there 
		if carry :

			res_lst.append(carry)

		#reverse the res list 
		res_lst.reverse()

		return res_lst



