"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""



nums = [2,3,-2,4]
out = 6 


nums2 = [-2,0,-1]
out2 = 0


class Solution():

	def maxProduct(self, nums) -> int:
		"""
		The function to find max product of subarray of the largest array 
		"""

		res = max(nums)

		curMin , curMax = 1,1

		for n in nums:

			if n == 0:
				curMin, curMax = 1,1 
				continue
			
			tmp = curMax *n
			curMax = max(n * curMax,n * curMin,n)
			curMin = min(tmp, n*curMin,n)

			res=max(res,curMax)

		return res 