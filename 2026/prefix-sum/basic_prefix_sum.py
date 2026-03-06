"""
The basics prefix sum 
"""

class Solution():

	def prefix_sum(self, nums):

		prefix = [0] * len(nums)

		for i in range(1,len(nums)):

			prefix[i] = prefix[i-1] + nums[i]

		return prefix


sol = Solution()

nums = [2,4,1,7,3]

print(sol.prefix_sum(nums))