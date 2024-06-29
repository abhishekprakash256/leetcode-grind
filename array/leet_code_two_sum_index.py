"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


"""
basic soln use 


1. soln
brute force 

run both the loops an  find the elements and give the elemnt 


2. optimal 

use a hash map 

store the to store the value seen and get the value of the remnaning subtratced value 
1,3,5,2,4



#edge case 

if len(nums) == 0 or len(nums) == 1:
	return None 



for i in range(len(nums) - 1):

	res = target - nums[i]

	if res in not mapper:
		mapper[res] = i

	else:
		return [i,mapper[res]]

return []


"""



class Solution():
	def twoSum(self,nums, target):
		"""
		The function to find the target values in the list
		"""

		#edge case 
		if len(nums) == 0 or len(nums) == 1:
			return None


		#make the hash map 
		mapper = {}

		#start the loop 
		for i in range(len(nums)):

			res = target - nums[i]

			if res not in mapper:
				mapper[nums[i]] = i

			else:
				return [i,mapper[res]]


		return []



