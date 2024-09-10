"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent 

houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

"""

"""
nums = [1,2,3,1]

out = 4 

Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.


nums = [2,7,9,3,1]
out = 12

Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""

"""

approach --- 


using the recursion -- 

base case 

helper(nums)
	if i == 0:
		rerturn nums[0]
	if i == 1:
		return max(nums[0],nums[1])


	return max(self.helper(nums(i) + self.helper(i-2)), self.helper(nums(i-1))





"""



class Solution:
	def helper_not_optim(self, nums: List[int], i: int) -> int:
		"""
		The helper function for the robber.
		It uses recursion to decide whether to rob house i or not.
		"""
		# Base case: when index i is out of bounds
		if i < 0:
			return 0

		# Recurrence relation: rob current house and skip the next, or skip this house
		return max(nums[i] + self.helper_not_optim(nums, i - 2), self.helper_not_optim(nums, i - 1))

	def rob_not_optimal(self, nums: List[int]) -> int:
		# Base cases
		if len(nums) == 0:
			return 0

		if len(nums) == 1:
			return nums[0]

		if len(nums) == 2:
			return max(nums[0], nums[1])

		n = len(nums)

		# Call the helper function starting from the last house (n-1)
		return self.helper_not_optim(nums, n - 1)
		


class Solution:
	def helper(self,nums,i,memo):
		"""
		The helper function 
		"""

		#base case 
		if i < 0:
			return 0

		if i in memo:
			return memo[i]

		res = max(nums[i] + self.helper(nums,i-2,memo), self.helper(nums,i-1,memo))
		
		memo[i] = res
		
		return res



	def rob(self,nums):
		"""
		The main funciton 
		accepted in leet code
		"""

		if len(nums) == 1:
			return nums[0]

		if len(nums) == 2:
			return max(nums[0],nums[1])

		memo = {}
		n = len(nums)

		self.helper(nums,n-1,memo)

		return memo[n-1]



	 

















