"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

"""


#test cases 
nums = [1,2,0]
out = 3 


nums2 = [3,4,-1,1]
out2 = 2


nums3 = [7,8,9,10,11]
out3 = 1




#-------------------------solution--------------------------#


class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		

		pass
		




if __name__ == "__main__":

	sol = Solution()

	res = sol.firstMissingPositive(nums)

	print(res)
