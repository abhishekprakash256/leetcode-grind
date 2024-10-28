
"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


"""

"""

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""


"""

nums.sort()

i , j = 0, len(target) - 1 





while i < j :

	curr_sum  = sum(nums[i:j + 1])

	if curr_sum > target:

		j -= 1
		i += 1

	elif curr_sum == target:

		return j-i

	else:

		return j - i



"""




class Solution_wrong:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		"""
		The function to find the minimum sum array
		"""

		#vars 
		i , j = 0 , len(nums) - 1

		while i < j :

			cur_sum = sum(nums[i:j+1])


			if cur_sum > target :

				j -= 1
				i += 1

			elif cur_sum == target:

				return j - i

			else:

				return j - i



"""
make the function to solve the minimum array 

"""

class Solution:
	def minSubArrayLen(self, target: int, nums: list) -> int:
		"""
		The fucnction to find the minimum size sub array
		"""

		#base case 
		if len(nums) == 1:
			if nums[0] < target:
				return 0 
			else:
				return 1
		

		#make the sliding window
		j = 1 
		min_length = float("inf")


		#start the loop 
		for i in range(len(nums)):

			curr_sum = nums[i] + nums[j]

			


			

		
