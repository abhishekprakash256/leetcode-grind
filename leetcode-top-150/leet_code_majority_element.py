"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


"""

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""


"""
optimal soln - 

single pass 

[2,2,1,1,1,2,2]

"""



class Solution:
	def majorityElement_brute(self, nums) -> int:
		"""
		The functtion to find the majority element
		passes leetcode but slow
		"""

		#base case 
		if len(nums) == 1:
			return nums[0]


		#make the mapper 
		mapper = {}

		#start the freq table 
		for i in nums:

			if i not in mapper:
				mapper[i] = 1

			else:
				mapper[i] = mapper[i] + 1


		mapper = sorted(mapper.items(), key=lambda x:x[1])

		
		return mapper[len(mapper)-1][0]


	def majorityElement_brute_2(self, nums: List[int]) -> int:
		nums.sort()
		n = len(nums)
		return nums[n//2]









sol = Solution()
print(sol.majorityElement_brute([3,3,4]))