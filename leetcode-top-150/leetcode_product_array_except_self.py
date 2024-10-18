"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

"""
Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""


"""
nums = [1,2,3,4]

prefix = [1,2,6,24]

postfix = [24,24,12,4]

output = [24,12,8,6]


how to make the output array -- 


out = [postfix[1],prefix[0]*postfix[2],prefix[1]*postfix[len(postfix)-1],prefix[len(prefix)-2]]
"""



class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""

		#make the array
		prefix = [nums[0]]
		postfix = [nums[len(nums)-1]]
		out = []



		#compute the prefix array 
		for i in range(1,len(nums)):

			prefix_val = prefix[i] * prefix[i-1]
			prefix.append(prefix_val)


		#compute the postfix array 
		for i in range(len(nums)-2,-1,0):

			postfix_val = postfix[i] * postfix[i+1]
			postfix.insert(0,postfix_val)


		#compute the final array

		print(prefix)
		print(postfix)


sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))







