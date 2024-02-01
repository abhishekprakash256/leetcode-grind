"""
find the maximum sub array in the of length k in the array, all the elements should be distinct 
"""


class Solution():

	#the correct solution of the program 
	def maximumSubarraySum(self, nums, k):
		l = 0
		r = 0
		max_sum = 0
		current_sum = 0
		unique_elements = set()

		while r < len(nums):
			if nums[r] not in unique_elements:
				unique_elements.add(nums[r])
				current_sum += nums[r]
				r += 1
			else:
				unique_elements.remove(nums[l])
				current_sum -= nums[l]
				l += 1

			if r - l == k:
				max_sum = max(max_sum, current_sum)
				unique_elements.remove(nums[l])
				current_sum -= nums[l]
				l += 1

		return max_sum

