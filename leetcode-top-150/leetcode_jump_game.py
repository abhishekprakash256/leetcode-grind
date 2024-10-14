"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

"""
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

"""



"""
brute force appraoch -- 


[2,3,1,1,4]

[3,2,1,0,4]

[3,2,1,0,4]






"""


class Solution1():
	def canJump(self, nums: List[int]) -> bool:
		"""
		The function to solve the jump problem
		passes leetcode

		"""
		reach = 0

		for i in range(0, len(nums)):

			if i > reach:
				return False
			if reach >= len(nums):
				return True
			if i + nums[i] > reach:
				reach = i + nums[i]

		return True



class Solution2():

	def canJump(self,nums):
		"""
		The function to find the brute force soln of can jump 
		passes leetcode

		"""

		gas = 0 

		for n in nums:

			if gas < 0 :
				return False
		
			elif gas < n:
				gas = n 
			
			gas -=1
		
		return True





class Solution():

	def canJump(self,nums):
		"""
		The function to make the car jump problem
		passes leet code

		"""

		gas = 0 


		for n in nums:

			

			if gas < 0:
				return False
			
			gas = max(n,gas)

			gas -= 1


		return True



