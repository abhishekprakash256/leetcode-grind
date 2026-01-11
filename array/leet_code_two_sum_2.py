"""
question --> 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



"""



"""

Approach -- 

dict to store the data 

how to get index ? 

make a index dict in one pass 

{3:0, 2:1 , 4:2}

next pass over the list and searh for diff in dict





"""

class Solution:
	def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
		"""
		The function to find the sum of the two numbers
		"""

		#the return list
		res = []
		

		for i in range(len(nums)):

			left = target - nums[i]

			for j in range(i+1,len(nums)):

				if nums[j] - left == 0 :

					res.append(i)
					res.append(j)

					return res


	def twoSum(self, nums: List[int], target: int) -> List[int]:
		"""
		The function to find the sum of the two numbers
		the optim solution
		"""

		#the index dict
		mapper = {}

		#res list
		res = []

		#make the index dict
		for i, num in enumerate(nums):

			left = target - num

			if left in mapper :

				return [mapper[left] , i]

			mapper[num] = i