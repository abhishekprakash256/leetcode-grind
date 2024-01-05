"""
the house can not be robbed in adjacent houses
the list is also a circle
"""


class Solution():

	def rob(self,nums):
		"""
		the function to find the rob value
		"""
		max(nums[0],self.helper(nums[1:]) , self.helper(nums[:-1]))



	def helper(self,nums):

		rob1, rob2 =0,0

		for n in nums:

			newRob = max(rob1 + n,rob2)
			rob1 = rob2
			rob2 = newRob

		return rob2