"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

#test case 

nums = [1,3,4,2,2]
out = 2 



class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		slow, fast = 0,0 

		while True :

			slow = nums[slow]
			fast = nums[nums[fast]]

			if slow == fast : 
				break 


		slow2 = 0 

		while True:

			slow = nums[slow]
			slow2 = nums[slow2]

			if slow == slow2: 
				return slow



if __name__ == "__main__":

	sol = Solution()

	res = sol.findDuplicate(nums)

	print(res)