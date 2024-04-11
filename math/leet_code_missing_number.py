"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing 
from the array.

"""

"""
given an array the number can be from range 0 to n 

so len can tell the total number we expect 

#brute force 

sorting 
and find missing in the step 

Onlogn

hash map O(n) space 


O(n) runtime  and O(1) space 



Input: nums = [3,0,1]
Output: 2


#sum apparch 

sum the first num from inclusiev array 

the sum the array 

subtract the both 



"""

class Solution:
	def missingNumber(self, nums) -> int:
		"""
		The function to find the missing value
		"""

		sum1,sum2 = 0 ,0 

		for i in range(len(nums)+1):

			sum1 +=i 

		for j in nums:

			sum2 +=j 

		
		return sum1 - sum2

		