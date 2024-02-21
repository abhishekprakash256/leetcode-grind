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




"""




class Solution():

	def helper(self,i,nums):
		"""
		The function to find the jumps reaching end of list

		"""
		#base case 
		if i == len(nums) - 1:
			return True

		for jumps in range(i+1):

			self.helper(jumps,nums)

		return False


	def canJump(self,nums):
		"""
		The main function 
		"""

		#constraints 
		if not nums:
			return None


		res = False

		for i in nums:

			res = self.helper(i,nums)

			if res == True:
				return True

		return res

sol = Solution()


res = sol.canJump(nums2)

print(res)












