"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.


"""


nums = [10,9,2,5,3,7,101,18]
out = 4

nums2 = [0,1,0,3,2,3]
out2 = 4 



class Solution():

	def lengthOfLIS(self,nums):
		"""
		The function to find the longest increasing subsequent string
		"""

		