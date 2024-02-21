"""
You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""


nums = [2,3,1,1,4]
out = True

nums2 = [3,2,1,0,4]
out2 = False



"""
algo -- 

basic approach recursion -- 


def helper(i,nums):

	if i == len(nums) - 1:
		return True 

	else:
		return False

	for jumps in range(n+1):
		
		self.helper(jumps,nums)

def canJump(self,nums):

	if not nums:
		return None 
	
	res = False

	for i in nums:

		if res == True:
			return True 

		res = self.helper(i,nums)


	return res



"""

class Solution():

	def helper(self,)
