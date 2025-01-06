"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money 
tashed, the only constraint stopping you from robbing each of them is that adjacent houses have security 
systems connected and it will automatically contact the police if two adjacent houses were broken into on 
the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of
money you can rob tonight without alerting the police.

"""

"""
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


"""


"""

approach -- 

using the dp and two pointer before

"""

class Solution_wrong():

	def rob(self,nums) :
		"""
		The function to find the house robber 
		"""

		#base case 
		if len(nums) == 1:

			return nums[0]


		#make the dp array ]
		nums.insert(0,0)
		nums.insert(0,0)

		for i in range(2,len(nums)-1) :

			nums[i] = nums[i] + nums[i-2]

			nums[i+1] = nums[i+1] + nums[i-1]

		return nums[-1]




class Solution():

	def __init__(self):

		self.memo = {}


	def helper(self):
		"""
		The function to make the helper
		"""


	def rob(self,nums):
		"""
		The function to find the rob house 
		"""

		