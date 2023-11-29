"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

#Test cases 

nums = [1,4,3,5]
target = 7
out = [1,2]


nums2 = [1,2,5,3,7]
target2 = 6
out2 = [0,2]


nums3 = [0,3]
target3 = 3
out3 = [0,1]


class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""

		mapper = {}

		if len(nums) == 1 or len(nums) == 0:

			return None

		for i in range(len(nums)):

			res = target - nums[i]

			if res not in mapper:

				mapper[res] = i


			else:

				return [mapper[target - res],i]
			
			print(mapper)


		return False



if __name__ == "__main__":

	sol = Solution()
	res = sol.twoSum(nums2,target2)

	print(res)